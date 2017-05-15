### rethow()

作用:检测出 err 后直接抛出

### maybeCallback(cb)

作用:检测cb是否为一个函数
实现逻辑:引入util模块,使用`util.isFunction(cb)`来检测cd是否为一个函数,如果为函数,则返回cb本身,如果不为函数,则返回rethow()


### fs.readFile = function(path,options,callback_)

作用:读文件的主要函数
实现逻辑:  
1. 调用maybecallback函数,返回一个callback函数.
1. 检测options参数是否存在:
  * 引入util模块,调用`util.isFunction(options)`来判断,如果存在:
      * 如果是函数或者不存在,options 为{ encoding: null, flag: 'r' }
      * 如果是字符串(使用`util.isString(options)`来检测),  options = { encoding: options, flag: 'r' };
      * 如果不是个对象(使用`util.isObject(options)`来实现),抛出错误,提示类型错误.
  * 如果不存在,该位置参数应该是callback函数.
1. 判断options中的encoding是否为合法的编码吗格式(使用assertEncoding函数来实现)
  * 引入buffer模块,使用`buffer.isEncoding(encoding)`来检测encoding是否为一个合法的编码格式.如果encoding存在但不是一个合法的编码格式,抛出 'Unknow encoding'错误.
1. 判断options 中的flag是否被定义,如果没有,则使用默认值"r",如果定义,则使用定义的内容.
1. 打开文件:fs.open(path,flag,438,function(er,fd_){...})
  * function(er,fd_){...}中:
  * 如果存在err,则直接返回callback(er)
  * fd = fd_
  * 
