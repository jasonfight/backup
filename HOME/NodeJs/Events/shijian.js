const EventEmitter = require('events').EventEmitter;
const event = new EventEmitter;

var event1 = function(){
  console.log('event1 running...');
  //event.removeListener('event2',event2);
  event.removeAllListeners('event2');
}
var event2 = function(){
  console.log('event2 running');
  //event.removeListener('event1',event1)
  event.removeAllListeners('event1');
}

event.on('event1',event1);
event.on('event2',event2);


event.emit('event1');
event.emit('event2');
