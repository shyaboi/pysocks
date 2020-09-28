
$('#onButt').click(function(e) {
  let keyPressed = e.keyCode
  console.log(keyPressed)
  $.post("/on", {'lightOn':1},(data)=> {
console.log(data)
  });
});

$('#onButt').click(function(e) {
  $.post("/off", {'lightOff':1},(data)=> {
console.log(data)
  });
});
