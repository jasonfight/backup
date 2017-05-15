var EventEmitter = require('events').EventEmitter;

var event = new EventEmitter();

var m = 0;

event.once('ABCD', (a, b) => {
  console.log(++m);
});


event.emit('ABCD', 'a', 'b');
event.emit('ABCD', 'a', 'b');
event.emit('ABCD', 'a', 'b');
