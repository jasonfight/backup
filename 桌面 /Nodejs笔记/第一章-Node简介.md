### Node.js优点:

1. 采用事件驱动,异步编程,为网络服务而设计,JavaScript的匿名函数和闭包特性非常适合事件驱动和异步编程.
1. Node.js非阻塞模式的I/O处理给NodeJs带来在相对低系统资源耗用下的高性能与出众的负载能力,非常适合用作依赖其他IO资源的中间层服务
1. Node.js轻量高效,可以认为是**数据密集型分布式部署环境**下的实时应用系统的完美解决方案,Node.js非常适合以下情况:在响应客户端之前,预计有很高的流量,但所需要的服务端逻辑和处理不一定很多.

### Node.js缺点:

1. 可靠性低
1. 单进程,单线程,只支持单核CPU,但是可以通过代码的健壮性来弥补.

### Node.js支持多进程的方式(Node.Js缺点的结局按方案)

1. 开启多个进程,每个进程绑定不同的端口,用反向代理服务器做负载均衡(例如Nginx),可以通过Nginx做一些过滤检查之类的工作,同时能够实现比较好的均衡策略,但有一个缺点,就是引入了一个中间层.
1. 多进程绑定在同一个端口监听,在Node.js中,提供了进程间发送文件句柄的功能,可以实现此功能.
1. 一个进程负责监听和接收连接,然后将收到的连接平均发送到子进程中去处理,Node.js内置了cluster库,可以直接支持多进程运行方式,


> 文件句柄: 程序打开一个文件时,返回的数字,接收到文件句柄的程序可以跟文件进行对话.

名称|文件句柄
---|:---:
stdin|0  
stdout|1
stderr|2
正常文件打开|3


### 异步式I/O与事件驱动

Node.js最大的特点就是采用异步式I/O与事件驱动的架构设计,对于高并发的解决方案,传统的架构是**多线程模型**,也就是为每个业务逻辑提供一个系统线程,通过系统线程切换来弥补同步式I/O调用时的时间开销,Node.js使用的是**单线程模型**,对于所有的I/O都采用异步的请求方式,避免了频繁的上下文切换,Node.js在执行的过程中会维护一个事件队列,程序在执行时进入事件循环,等待下一个事件的到来,每个异步式I/O请求完成后会被推送到事件队列,等待程序进程进行处理,

### Node.js的安装

#### ubuntu安装方法:
```bash
$ curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
开发环境的安装:

```bash
$ sudo apt-get install -y build-essential
```

### npm的使用

npm是随同NodeJsNode.js一起安装的包管理工具,常见的使用场景有如下几种:
* 允许用户从NPM服务器下载第三方库到本地
* 允许用户从NPM服务器下载别人编写的命令行程到本地使用
* 允许用户将自己编写的包或命令行程序上传到NPM服务器供他人使用

### npm的安装

```bash
npm install express   # 本地安装,在本地生成node_modules的文件夹,可以通过require()来引入本地安装的包
npm install express -g #全局安装,在~/.npm/express中,生成对应版本号命名的文件夹.
```
#### 查看全局安装的模块

```bash
$ npm ls -g
```
### 强制重新安装

```bash
$ npm install <packageName> --force
```
### 更新已经安装的模块

```bash
$ npm update <packageName>
```

### package.json

#### scripts字段

`scripts`制定了运行脚本命令的npm命令行缩写,比如`start`制定了运行`npm runstart` 时,所要执行的命令.

#### dependencies字段与devDependencies字段

  `dependencies`字段指定了**项目运行**所以来的模块,`devDependencies`指定**项目开发**所需要的模块.都指向一个对象,该对象的各个成员,分别有模块名和队形的版本要求组成,表示依赖的模块及其版本范围.

  版本范围的规定:

  > 指定版本:eg:1.2.2,安装时只能安装指定版本  
  > 波浪号 ~ :eg:~1.2.2,安装1.2.x的最新版本,不包括1.3.x,  
  > 插入号 ^ : eg:^1.2.2,安装1.x.x的最新版本,不包括2.x  
  > latest: 最新版本.

#### 自动生成package.json文件

```bash
$ npm init
$ npm init --Yes
```
其中,`name`和`version`是必填的,其余选填.

有了`package.json`文件,就可以直接使用`npm install`命令,在当前目录中安装所需要的模块.

如果一个模块不在package.json中,可以单独安装这个模块,并加入package.json中

```bash
$ npm install <packageName> --save #写入dependencies属性
$ npm install <packageName> --save-dev #写入devDependencies属性
```

### Node.js升级

Node.js有一个模块叫`n`,专门用来管理Node.js的版本安装,并将当前的版本省纪委`stable`最新版本

```bash
$ npm install -g n   #安装n
$ npm n stable      # 升级到stable版本
```

显示当前版本信息
```bash
$ node -v
$ npm -v
```
### nvm的使用

nvm类似于python中的virtualenv或者ruby中的rvm,每个node版本的模块都会被安装在各自版本的沙箱中,

### nvm的安装
```bash
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh | bash
```
#### 查看远程Node.js的版本信息
```bash
$ nvm ls-remote
```
#### 查看本地所有Node.js的版本信息
```bash
$ nvm ls
```
