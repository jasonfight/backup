## Node.js 基础知识

### 1.为什么要用node?

1. 采用事件驱动、异步编程，为网络服务而设计。其中Javascript的匿名函数和闭包特性非常适合事件驱动、异步编程。而且JavaScript也简单易学，很多前端设计人员可以很快上手做后端设计。
1. Node.js非阻塞模式的IO处理给Node.js带来在相对低系统资源耗用下的高性能与出众的负载能力，非常适合用作依赖其它IO资源的中间层服务。
1. Node.js轻量高效，可以认为是数据密集型分布式部署环境下的实时应用系统的完美解决方案。Node非常适合如下情况：在响应客户端之前，您预计可能有很高的流量，但所需的服务器端逻辑和处理不一定很多。

### 2.node的构架是什么样子的?
主要分为三层，应用app >> V8及node内置架构 >> 操作系统. V8是node运行的环境，可以理解为node虚拟机．node内置架构又可分为三层: 核心模块(javascript实现) >> c++绑定 >> libuv + CAes + http.

### 3.node有哪些核心模块?
1. process：提供进程间通信的基本功能
1. URL：用于处理URL及URL中的查询串
1. console:提供基本的输出功能
1. event：相关事件的处理
1. File System： 对文件与目录的创建、删除、权限设置及操作，
1. Buffer:

### 4.node有哪些全局对象?

1.  process
1.  console
1.  Buffer
1.  exports

### 5.process有哪些常用方法?

1. processstdin
1. process.stdout
1. process.stderr
1. process.on
1. process.env
1. process.argv
1. process.arch
1. process.platform
1. process.exit

### 6.console有哪些常用方法?
1. console.log
1. console.info
1. console.error
1. console.warning
1. console.time
1. console.timeEnd
1. console.trace
1. console.table



### 7.node有哪些定时功能?
setTimeout/clearTimeout：设置超时定时器/清除超时定时器

setInterval/clearInterval：设置预定定时器(一段时间执行一次)/清除预定定时器

setImmediate/clearImmediate：设置预定定时器(立即执行)/清除预定定时器

process.nextTick：定义出一个动作，并且让这个动作在下一个事件轮询的时间点上执行,
process.nextTick()定义的调用会创建一个新的子堆栈。在当前的栈里，你可以执行任意多的操作。但一旦调用netxTick，函数就必须返回到父堆栈。然后事件轮询机制又重新等待处理新的事件，如果发现nextTick的调用，就会创建一个新的栈。

##Node.js 事件

### 1.Promise 中 .then 的第二参数与 .catch 有什么区别?
当参数中的第一个函数需要抛出一个错误时,.then的第二参数不会捕捉第一参数抛出的错误.

### 2.Eventemitter 的 emit 是同步还是异步?
同步的.事件监听器通过同步方式,确保所有的监听器能够顺序的注册,从而确保正确的事件排序,避免出现逻辑错误.


### 3.如何判断接口是否异步? 是否只要有回调函数就是异步?

判断:
* console.log 打印
* 看是否有 IO 操作
单纯使用回调函数并不会异步, IO 操作才可能会异步, 除此之外还有使用 setTimeout 等方式实现异步

### 4.nextTick, setTimeout 以及 setImmediate 三者有什么区别?

setImmediate()属于check观察者，其设置的回调函数，会插入到下次事件循环的末尾。
setImmediate()属于check观察者，其设置的回调函数，会插入到下次事件循环的末尾。
process.next()所设置的回调函数会存放到数组中，一次性执行所有回调函数。
setImmediate()所设置的回调函数会存到到链表中，每次事件循环只执行链表中的一个回调函数。

根据setTimeout()实现的源码,执行setTimeout(fn, 0)其实就是在执行setTimeout(fn, 1)，也就是说setImmediate()是有可能先于setTimeout(fn, 0)执行的.


### 5.如何实现一个 sleep 函数?
```js
function sleep(ms) {
  var start = Date.now(), expire = start + ms;
  while (Date.now() < expire) ;
  return;
}
```
### 6.如何实现一个异步的 reduce? (注:不是异步完了之后同步 reduce)
需要了解 reduce 的情况, 是第 n 个与 n+1 的结果异步处理完之后, 在用新的结果与第 n+2 个元素继续依次异步下去

### 7.node中的事件循环是什么样子的?

```
   ┌───────────────────────┐
┌─>│        timers         │
│  └──────────┬────────────┘
│  ┌──────────┴────────────┐
│  │     I/O callbacks     │
│  └──────────┬────────────┘
│  ┌──────────┴────────────┐
│  │     idle, prepare     │
│  └──────────┬────────────┘      ┌───────────────┐
│  ┌──────────┴────────────┐      │   incoming:   │
│  │         poll          │<─────┤  connections, │
│  └──────────┬────────────┘      │   data, etc.  │
│  ┌──────────┴────────────┐      └───────────────┘
│  │        check          │
│  └──────────┬────────────┘
│  ┌──────────┴────────────┐
└──┤    close callbacks    |
   └───────────────────────┘
```



### 8.什么是EventEmitter?

EventEmitter是node中一个实现观察者模式的类，主要功能是监听和发射消息，用于处理多模块交互问题.

### 9.如何实现一个EventEmitter?

主要分三步：定义一个子类，调用构造函数，继承EventEmitter
```js
var util = require('util');
	var EventEmitter = require('events').EventEmitter;

	function MyEmitter() {
		EventEmitter.call(this);
	} // 构造函数

	util.inherits(MyEmitter, EventEmitter); // 继承

	var em = new MyEmitter();
	em.on('hello', function(data) {
		console.log('收到事件hello的数据:', data);
	}); // 接收事件，并打印到控制台
	em.emit('hello', 'EventEmitter');
```


### 10.EventEmitter有哪些典型应用?

1. 模块间传递消息
2. 回调函数内外传递消息
3. 处理流数据，因为流是在EventEmitter基础上实现的.
4. 观察者模式发射触发机制相关应用

### 11.怎么捕获EventEmitter的错误事件?

 监听error事件即可．如果有多个EventEmitter,也可以用domain来统一处理错误事件
```js
  var domain = require('domain');
    var myDomain = domain.create();
    myDomain.on('error', function(err){
        console.log('domain接收到的错误事件:', err);
    }); // 接收事件并打印
    myDomain.run(function(){
        var emitter1 = new MyEmitter();
        emitter1.emit('error', '错误事件来自emitter1');
        emitter2 = new MyEmitter();
        emitter2.emit('error', '错误事件来自emitter2');
    });
```

### 12.EventEmitter中的newListenser事件有什么用处?

newListener可以用来做事件机制的反射，特殊应用，事件管理等．当任何on事件添加到EventEmitter时，就会触发newListener事件，基于这种模式，我们可以做很多自定义处理.

```js
var emitter3 = new MyEmitter();
emitter3.on('newListener', function(name, listener) {
	console.log("新事件的名字:", name);
	console.log("新事件的代码:", listener);
	setTimeout(function(){ console.log("我是自定义延时处理机制"); }, 1000);
});
emitter3.on('hello', function(){
	console.log('hello　node');
});

```
