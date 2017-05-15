## Node.js基础知识
### 一. 为什么要用node?
 1. 采用事件驱动、异步编程，为网络服务而设计。其实Javascript的匿名函数和闭包特性非常适合事件驱动、异步编程。而且JavaScript也简单易学，很多前端设计人员可以很快上手做后端设计。
 1. Node.js非阻塞模式的IO处理给Node.js带来在相对低系统资源耗用下的高性能与出众的负载能力，非常适合用作依赖其它IO资源的中间层服务
 1. Node.js轻量高效，可以认为是数据密集型分布式部署环境下的实时应用系统的完美解决方案。Node非常适合如下情况|在响应客户端之前，您预计可能有很高的流量，但所需的服务器端逻辑和处理不一定很多。


### 二. node的构架是什么样子的?

### 三. node有哪些核心模块?

模块名称|模块简介
---|---
os 系统基本信息|os模块可提供操作系统的一些基本信息
process 进程管理|是一个全局变量.无需 require
fs 文件管理|对文件进行读写等操作
url 文件管理|解析url,解析主机,将json数组逆向成url
util 使用工具|提供常用函数的集合，用于弥补核心JavaScript的一些功能过于精简的不足。并且还提供了一系列常用工具，用来对数据的输出和验证
event事件|处理各种事件,有异步和同步两种方法

<!-- [原文连接](http://cnodejs.org/topic/548e53f157fd3ae46b2334fd) -->



### 四. node有哪些全局对象?

1. `global`|是个nodejs最大的父对象。
1. `__dirname`|是当前执行的js文件的所在的目录路径。
1. `__filename`|是当前执行的js的全路径，包含js文件所在的目录路径和文件名称。


### 五. process有哪些常用方法?
方法|简介
---|---
platform|判断当前系统平台
argv|当前进程的命令行参数数组
execPath|当前进程的可执行文件的绝对路径
stdout|指向标准输出
stdin|指向标准输入
stderr|指向标准错误
stderr|指向标准错误
cwd|返回运行当前脚本的工作目录的路径
abort|立即结束进程
nextTick| 指定下次事件循环首先运行的任务
process|支持的一些事件,通过一些事件，我们可做一些友好的提示或者处理。
uncaughtException|当前进程抛出一个没有被捕捉的意外时，会触发uncaughtException事件
message| 接受来自父进程的消息
rejectionHandled|用于捕获与它关联的promise错误处理并且产生的reject
unhandledRejection| 同理这个便是用于捕获没有与之关联promise错误处理的reject

### 六. console有哪些常用方法?
1. console.assert(expression, object[, object...])
接收至少两个参数，第一个参数的值或返回值为false的时候，将会在控制台上输出后续参数的值

1. console.count([label])
输出执行到该行的次数，可选参数 label 可以输出在次数之前

1. console.dir(object)
将传入对象的属性，包括子对象的属性以列表形式输出

1. console.error(object[, object...])
用于输出错误信息，用法和常见的console.log一样，不同点在于输出内容会标记为错误的样式，便于分辨

1. console.group
这是个有趣的方法，它能够让控制台输出的语句产生不同的层级嵌套关系，每一个console.group()会增加一层嵌套，相反要减少一层嵌套可以使用console.groupEnd()方法


### 七. node有哪些定时功能?
1. setTimeout(匿名函数,毫秒数) 表示多少毫秒后触发一次此匿名函数.
1. setInterval(匿名函数,毫秒数)  表示多少毫秒后重复触发此匿名函数.
1. setImmediate(匿名函数,[参数])


## Node.js事件
### 一. Promise 中 .then 的第二参数与 .catch 有什么区别?

then方法是定义在原型对象Promise.prototype上的。它的作用是为Promise实例添加状态改变时的回调函数。

then方法返回的是一个新的Promise实例(注意，不是原来那个Promise实例)。因此可以采用链式写法，即then方法后面再调用另一个then方法
Promise.prototype.catch方法是.then(null,rejeaction)的别名，用于指定发生错误时的回调函数





### 二. Eventemitter 的 emit 是同步还是异步?

EventEmitter只是个观察者模式，和消息队列没啥关系，增加/删除listener，以及在emit的时候回调listener这才是它的本质。所以它的函数执行是同步的。


三. 如何判断接口是否异步? 是否只要有回调函数就是异步?

### 四. nextTick, setTimeout 以及 setImmediate 三者有什么区别?

1. setTimeout()
setTimeout（setInterVal和setTimeout函数区别只是执行次数）函数，需要注意的是，setTimeout()只是将事件插入了"任务队列"，必须等到当前代码（执行栈）执行完，主线程才会去执行它指定的回调函数。要是当前代码耗时很长，有可能要等很久，所以并没有办法保证，回调函数一定会在setTimeout()指定的时间执行。

1. setImmediate()
setImmediate()是将事件插入到事件队列尾部，主线程和事件队列的函数执行完成之后立即执行setImmediate指定的回调函数，和setTimeout(fn,0)的效果差不多，但是当他们同时在同一个事件循环中时，执行顺序是不定的。

1. process.nextTick()
process.nextTick()方法可以在当前"执行栈"的尾部-->下一次Event Loop（主线程读取"任务队列"）之前-->触发process指定的回调函数。也就是说，它指定的任务总是发生在所有异步任务之前，当前主线程的末尾。（nextTick虽然也会异步执行，但是不会给其他io事件执行的任何机会）

五. 如何实现一个 sleep 函数?
使用调用自定义函数的方式消耗时间：
```js
function sleep(numberMillis) {
var now = new Date();
var exitTime = now.getTime() + numberMillis;
while (true) {
now = new Date();
if (now.getTime() > exitTime)
return;
}
}
```

### 六. 如何实现一个异步的 reduce? (注:不是异步完了之后同步 reduce)

### 七. node中的事件循环是什么样子的?
事件循环能让 Node.js 执行非阻塞 I/O 操作 -- 尽管JavaScript事实上是单线程的 -- 通过在可能的情况下把操作交给操作系统内核来实现。

由于大多数现代系统内核是多线程的，内核可以处理后台执行的多个操作。当其中一个操作完成的时候，内核告诉 Node.js，相应的回调就被添加到轮询队列（poll queue）并最终得到执行。


### 八. 什么是EventEmitter?
  EventEmitter是Node.js中事件的核心对象，所有的事件基本都是通过这个对象完成构建的！这是非常之重要的对象，而且没有之一。

### 九. 如何实现一个EventEmitter?
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
  	em.emit('hello', 'EventEmitter传递消息真方便!');
```

### 十. EventEmitter有哪些典型应用?
*  模块间传递消息
*  回调函数内外传递消息
*  处理流数据，因为流是在EventEmitter基础上实现的.
*  观察者模式发射触发机制相关应用

### 十一. 怎么捕获EventEmitter的错误事件?
监听error事件即可．如果有多个EventEmitter,也可以用domain来统一处理错误事件.
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
	em.emit('hello', 'EventEmitter传递消息真方便!');
  ```

### 十二. EventEmitter中的newListenser事件有什么用处?
newListener可以用来做事件机制的反射，特殊应用，事件管理等．当任何on事件添加到EventEmitter时，就会触发newListener事件，基于这种模式，我们可以做很多自定义处理.

```js
var emitter3 = new MyEmitter();
emitter3.on('newListener', function(name, listener) {
	console.log("新事件的名字:", name);
	console.log("新事件的代码:", listener);
	setTimeout(function(){ console.log("我是自定义延时处理机制");}, 1000);
});
emitter3.on('hello', function(){
	console.log('hello　node');
});
```
