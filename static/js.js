const w = 119
const a = 97
const s = 115
const d = 10
const l = 108
const space = 32

$(document).keypress(function(e) {
  let keyPressed = e.keyCode
  console.log(keyPressed)
  if (keyPressed==w){ 
  $.post("/w", {'forward':1},(data)=> {
    console.log(data)
  });}
  if (keyPressed==a){ 
    $.post("/a", {'left':1},(data)=> {
      console.log(data)
    });}
    if (keyPressed==space){ 
      $.post("/off", {'lightOff':1},(data)=> {
        console.log(data)
      });}
});


$('#onButt').click(function(e) {
  $.post("/on", {'lightOn':1},(data)=> {
console.log(data)
  });
});


$('#offButt').click(function(e) {
  $.post("/off", {'lightOff':1},(data)=> {
console.log(data)
  });
});
