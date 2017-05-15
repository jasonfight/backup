var db = require('./index');

var user1 = new db.User({
  account:'String',
  name:'String',
  password:'String',
  email:'String',
  age:20,
  gender:'String',
  birthday:'1992/02/01',

});


user1.save(function(err){
  if (err) {
    console.log(err);
  }else{
    console.log('chenggong');
  }
})
