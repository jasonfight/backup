const EventMitter = require('events').EventMitter;


var a = 1;
const b = a;
console.log(b);
a = 2;
b = a;
console.log(b);
