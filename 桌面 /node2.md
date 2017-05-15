### 1 什么是EventEmitter?
EventEmitter是node中一个实现观察者模式的类，主要功能是监听和发射消息，用于处理多模块交互问题.

### 2 如何实现一个EventEmitter?
主要分三步：定义一个子类，调用构造函数，继承EventEmitter
```js
var util = require('util');
	var EventEmitter = require('events').EventEmitter;

	function MyEmitter() {
		EventEmitter.call(this);
	} 

	util.inherits(MyEmitter, EventEmitter); // 继承

	var em = new MyEmitter();
	em.on('hello', function(data) {
		console.log('收到事件hello的数据:', data);
	}); 
	em.emit('hello', 'EventEmitter....');
```
### 3 EventEmitter有哪些典型应用?
* 模块间传递消息 
* 回调函数内外传递消息 
* 处理流数据，因为流是在EventEmitter基础上实现的. 
* 观察者模式发射触发机制相关应用


### 4 怎么捕获EventEmitter的错误事件?
监听error事件即可．如果有多个EventEmitter,也可以用domain来统一处理错误事件.

```js
	var domain = require('domain');
	var myDomain = domain.create();
	myDomain.on('error', function(err){
		console.log('domain接收到的错误事件:', err);
	}); 
	myDomain.run(function(){
		var emitter1 = new MyEmitter();
		emitter1.emit('error', '错误事件来自emitter1');
		emitter2 = new MyEmitter();
		emitter2.emit('error', '错误事件来自emitter2');
	});
```
### 5 什么是Stream,有什么好处
stream是基于事件EventEmitter的数据管理模式．由各种不同的抽象接口组成，主要包括可写，可读，可读写，可转换等几种类型．

非阻塞式数据处理提升效率，片断处理节省内存，管道处理方便可扩展等.

### 6 Stream有哪些典型应用?
文件，网络，数据转换，音频视频等.

###  7 node的网络模块架构是什么样子的,node是怎样支持https,tls的
node全面支持各种网络服务器和客户端，包括tcp, http/https, tcp, udp, dns, tls/ssl等.

实现支持https,tls,主要实现以下几个步骤即可: 
* openssl生成公钥私钥 
* 服务器或客户端使用https替代http 
* 服务器或客户端加载公钥私钥证书

### 8 为什么需要child-process?
node是异步非阻塞的，这对高并发非常有效．可是我们还有其它一些常用需求，比如和操作系统shell命令交互，调用可执行文件，创建子进程进行阻塞式访问或高CPU计算等，child-process就是为满足这些需求而生的．child-process顾名思义，就是把node阻塞的工作交给子进程去做．


### 9 两个node程序之间怎样交互?
使用fork，原理是子程序用process.on, process.send，父程序里用child.on,child.send进行交互.

```js

	1) fork-parent.js
	var cp = require('child_process');
	var child = cp.fork('./fork-child.js');
	child.on('message', function(msg){
		console.log('老爸从儿子接受到数据:', msg);
	});
	child.send('我是你爸爸，送关怀来了!');

	2) fork-child.js
	process.on('message', function(msg){
		console.log("儿子从老爸接收到的数据:", msg);
		process.send("我不要关怀，我要银民币！");
	});

```

### 10 mongoose是什么？有支持哪些特性?
mongoose是mongodb的文档映射模型．主要由Schema, Model和Instance三个方面组成．Schema就是定义数据类型，Model就是把Schema和js类绑定到一起，Instance就是一个对象实例．常见mongoose操作有,save, update, find. findOne, findById, static方法等．




