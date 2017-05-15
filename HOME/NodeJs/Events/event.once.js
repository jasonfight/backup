const EventEmitter = require('events')
const myEmitter = new EventEmitter();
// myEmitter.once('Event',function(){
myEmitter.once('Event',() => { //() => {} 相当于function(){},但是this会改变,不再是调用对象的空间,而是调用对象的上一层对象的空间
    console.log(this);
})
myEmitter.emit('Event');  //只会调用一遍,然后会注销该命名事件
myEmitter.emit('Event'); //该次调用不会生效
