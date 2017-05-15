var util = require('util');
var fs = require('fs');
var kMaxLength = 1073741823;

function rethrow() {

  // NOTE: 在调试模式下才起作用.一般直接到 return function(err)函数.

  return function(err) {
    if (err) {
      throw err;  // NOTE: 如果有异常,则直接抛出异常.
    }
  };

}
// NOTE: 检测参数是不是一个函数
function maybeCallback(cb) {
  return util.isFunction(cb) ? cb : rethrow();
}


function assertEncoding(encoding) {
  if (encoding && !Buffer.isEncoding(encoding)) {
    throw new Error('Unknown encoding: ' + encoding);
  }
}

fs.myreadFile = function(path, options, callback_) {
  var callback = maybeCallback(arguments[arguments.length - 1]);

  if (util.isFunction(options) || !options) {
    options = { encoding: null, flag: 'r' };
  } else if (util.isString(options)) {
    options = { encoding: options, flag: 'r' };
  } else if (!util.isObject(options)) {
    throw new TypeError('Bad arguments');
  }

  var encoding = options.encoding;
  assertEncoding(encoding);
  var size;
  var buffer; 
  var buffers; 
  var pos = 0;
  var fd;

  var flag = options.flag || 'r';
  fs.open(path, flag, 438 /*=0666*/, function(er, fd_) {
    if (er) return callback(er);
    fd = fd_;

    fs.fstat(fd, function(er, st) {
      if (er) {
        return fs.close(fd, function() {
          callback(er);
        });
      }

      size = st.size;
      if (size === 0) {
        // the kernel lies about many files.
        // Go ahead and try to read some bytes.
        buffers = [];
        return read();
      }

      if (size > kMaxLength) {
        var err = new RangeError('File size is greater than possible Buffer: ' +
            '0x3FFFFFFF bytes');
        return fs.close(fd, function() {
          callback(err);
        });
      }
      buffer = new Buffer(size);
      read();
    });
  });

  function read() {
    if (size === 0) {
      buffer = new Buffer(8192);
      fs.read(fd, buffer, 0, 8192, -1, afterRead);
    } else {
      fs.read(fd, buffer, pos, size - pos, -1, afterRead);
    }
  }

  function afterRead(er, bytesRead) {
    if (er) {
      return fs.close(fd, function(er2) {
        return callback(er);
      });
    }

    if (bytesRead === 0) {
      return close();
    }

    pos += bytesRead;
    if (size !== 0) {
      if (pos === size) close();
      else read();
    } else {
      buffers.push(buffer.slice(0, bytesRead));
      read();
    }
  }

  function close() {
    fs.close(fd, function(er) {
      if (size === 0) {
        buffer = Buffer.concat(buffers, pos);
      } else if (pos < size) {
        buffer = buffer.slice(0, pos);
      }

      if (encoding) buffer = buffer.toString(encoding);
      return callback(er, buffer);
    });
  }
};

module.exports.myreadFile= fs.myreadFile;
