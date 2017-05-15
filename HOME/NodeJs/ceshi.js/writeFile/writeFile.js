var fs = require('events');
const assertEncoding = internalFS.assertEncoding;
const util = require('util');
const { isUint8Array } = process.binding('util');

function maybeCallback(cb) {
  return typeof cb === 'function' ? cb : rethrow();
}


function getOptions(options, defaultOptions) {
  if (options === null || options === undefined ||
      typeof options === 'function') {
    return defaultOptions;
  }

  if (typeof options === 'string') {
    defaultOptions = util._extend({}, defaultOptions);
    defaultOptions.encoding = options;
    options = defaultOptions;
  } else if (typeof options !== 'object') {
    throw new TypeError('"options" must be a string or an object, got ' +
                        typeof options + ' instead.');
  }

  if (options.encoding !== 'buffer')
    assertEncoding(options.encoding);
  return options;
}


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
};

var mywriteFile = function(path, data, options, callback) {
  callback = maybeCallback(arguments[arguments.length - 1]);
  options = getOptions(options, { encoding: 'utf8', mode: 0o666, flag: 'w' });
  const flag = options.flag || 'w';

  if (isFd(path)) {
    writeFd(path, true);
    return;
  }

  function writeFd(fd, isUserFd) {
      var buffer = isUint8Array(data) ?
          data : Buffer.from('' + data, options.encoding || 'utf8');
      var position = /a/.test(flag) ? null : 0;

      writeAll(fd, isUserFd, buffer, 0, buffer.length, position, callback);
    }
  };

  fs.open(path, flag, options.mode, function(openErr, fd) {
    if (openErr) {
      callback(openErr);
    } else {
      writeFd(fd, false);
    }
  });

  function writeFd(fd, isUserFd) {
    var buffer = isUint8Array(data) ?
        data : Buffer.from('' + data, options.encoding || 'utf8');
    var position = /a/.test(flag) ? null : 0;

    writeAll(fd, isUserFd, buffer, 0, buffer.length, position, callback);
  }
};

module.exports.mywriteFile = mywriteFile;
