
const DEBUG = process.env.NODE_DEBUG && /fs/.test(process.env.NODE_DEBUG);
const Buffer = require('buffer').Buffer;
// const fs = exports;
var fs = require('fs');


function writeAll(fd, isUserFd, buffer, offset, length, position, callback_) {
  var callback = maybeCallback(arguments[arguments.length - 1]);

  // write(fd, buffer, offset, length, position, callback)
  fs.write(fd, buffer, offset, length, position, function(writeErr, written) {
    if (writeErr) {
      if (isUserFd) {
        callback(writeErr);
      } else {
        fs.close(fd, function() {
          callback(writeErr);
        });
      }
    } else {
      if (written === length) {
        if (isUserFd) {
          callback(null);
        } else {
          fs.close(fd, callback);
        }
      } else {
        offset += written;
        length -= written;
        if (position !== null) {
          position += written;
        }
        writeAll(fd, isUserFd, buffer, offset, length, position, callback);
      }
    }
  });
}


function isFd(path) {
  return (path >>> 0) === path;
}


function assertEncoding(encoding) {
  if (encoding && !Buffer.isEncoding(encoding)) {
    throw new Error('Unknown encoding: ' + encoding);
  }
}

function maybeCallback(bc){
   return typeof cb === 'function' ? cb : rethrow();
}


function throwOptionsError(options) {
  throw new TypeError('Expected options to be either an object or a string, ' +
    'but got ' + typeof options + ' instead');
}

function rethrow() {
  // Only enable in debug mode. A backtrace uses ~1000 bytes of heap space and
  // is fairly slow to generate.
  if (DEBUG) {
    var backtrace = new Error();
    return function(err) {
      if (err) {
        backtrace.stack = err.name + ': ' + err.message +
                          backtrace.stack.substr(backtrace.name.length);
        throw backtrace;
      }
    };
  }

  return function(err) {
    if (err) {
      throw err;  // Forgot a callback but don't know where? Use NODE_DEBUG=fs
    }
  };
}

var mywriteFile = function(path,data,options,callback_){
  var callback = maybeCallback(arguments[arguments.length-1]);

  if (!options || typeof options === 'function') {
  options = { encoding: 'utf8', mode: 0o666, flag: 'w' };
} else if (typeof options === 'string') {
  options = { encoding: options, mode: 0o666, flag: 'w' };
} else if (typeof options !== 'object') {
  throwOptionsError(options);
}
  assertEncoding(options.encoding);  //如果encoding有错误.则报错,如果没有错,不进行任何操作.

  var flag = options.flag || 'w';



  if (isFd(path)) {
    writeFd(path, true);
  return;
}


fs.open(path, flag, options.mode, function(openErr, fd) {
   if (openErr) {
     callback(openErr);
   } else {
     writeFd(fd, false);
   }
 });


var isUserFd = isFd(path);
 function writeFd(fd){
   var buffer = (data instanceof Buffer) ? data : new Buffer('' + data,
        options.encoding || 'utf8');
    var position = /a/.test(flag) ? null : 0;

    writeAll(fd, isUserFd, buffer, 0, buffer.length, position, callback);
 }

};

module.exports.mywriteFile = mywriteFile;
