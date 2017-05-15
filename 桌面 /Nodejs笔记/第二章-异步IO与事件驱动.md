### 异步IO与事件编程

阻塞模式下.一个贤臣只能处理一项任务,要想提高吞吐量必须通过多线程,  
在非阻塞模式下,一个线程永远在执行计算操作,这个线程所使用的CPU利用率永远是100%,IO以事件的方式通知.  
在阻塞模式下,多线程能提高吞吐量,因为一个线程阻塞时,还有其他的线程在工作,多线程可以让CPU资源不被阻塞的线程浪费.  
在非阻塞模式下,线程不会被IO阻塞,永远在利用CPU,多线程的好处仅仅是在多核的情况下利用多核,而Node.js的单线程也能做到这样的好处

### 阻塞和非阻塞

阻塞IO的特点是调用之后一定要等系统内核层面完成所有操作时,调用才结束.  
非阻塞IO是在调用之后立即返回,但此时完整的IO没有完成,立即返回的是当前调用的状态,为了获取完成的数据,应用程序需要重复调用IO操作来确认是否完成,这种重复调用判断操作是否完成的技术叫做轮询.

### read

用户进程发送read操作,如果kernel中的数据没有准备好,则不会阻塞用户进程,而是返回一个error,而用户进程在发起一个read操作后,立即得到了一个结果,如果是error,则继续发送read操作,一旦kernel中的数据准备好了,并且再次收到了用户进程的read操作指令,则立即将数据拷贝到用户内存,并返回.

### select

当用户进程调用了select操作,整个进程会被阻塞,同时,肯饿了会监听所有select负责的read,当任意一个read中的数据准备好了,read就会返回,此时用户进程再调用read,将数据从kernel拷贝到用户进程.

### epoll

用户进程发起read操作之后,将会进行休眠,直到事件将他唤醒,另一方便,在kernel角度上,当它收到一个 asynchronous read之后,首先会立即返回,所以不会阻塞进程,然后,kernel会等待数据完成,将数据拷贝到用户内存,完成之后,kernel会给用户进程发送一个signal,告诉他read操作完成了,FreeBSD是kqueque.

### 异步IO

异步IO是通过一个线程进行操作,将IO交给操作系统,完成后再通知用户进程,

### 回调函数


同步读取文件:
```js
var fs = require('fs');
var data = fs.readFileSync('file.md','utf-8')
console.log(data);
console.log('read file over...');
```
将file.md 的文件名作为参数传入readFileSync()函数中,阻塞等待读取完成后,将文件内容作为函数的返回值返回给data,然后输出data的值,再输出'read file over..'

异步读取文件
```js
var fs = require('fs');
fs.readFile('file.md','utf-8',function(err,data){
  if (err) {
    console.error(err);
  }else {
    console.log(data);
  }
});
console.log('read file over...');
```
