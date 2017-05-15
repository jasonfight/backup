## 流 Stream

流(Stream)在Node.js中是处理流数据的抽象接口.

Node.js提供了多种流对象,如`HTTP请求``process.stdout`

### 引入方式
`var stream  = require('stream')`

stream本省对于需要创建新的流的实例的开发者有用处,对于主要是消费流的开发者来说,很少使用`stream`模块.

### 流的类型

* Readable 可读的流
* Writable 可写的流
* Duplex 可读写的流
* Transform 在读写过程中可以修改和变换数据的Duplex流

### 对象模式

所有使用Node.jsAPI创建的流对象都只能操作`strings`和`Buffer`对象,但可以通过一些第三方流的实现,来处理其他类型的JavaScript的值(除过null),这些流被认为是工作在`对象模式`.

### 缓冲

`Writable`和`Readable`流后会将数据存在buffer中,然后通过`Writable._writableState.getBuffer()`或`readable._readableState.buffer`来获取,缓存的大小,取悦于传递给流构造函数的`highWaterMark`选项,对于普通的流,`highWaterMark`选项制定了总共的字节数,
