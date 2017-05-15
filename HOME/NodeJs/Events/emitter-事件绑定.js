// const EventEmitter = require('events');
// class MyEmitter extends EventEmitter{}
//上面两句代码等价于:  const MyEmitter = require('events').EventEmitter

const MyEmitter = require('events').EventEmitter
const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('发生了一个事件！');
});
myEmitter.emit('event');
