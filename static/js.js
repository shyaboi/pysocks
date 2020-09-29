const w = 119
const a = 97
const s = 115
const d = 100
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
  if (keyPressed==d){ 
      $.post("/d", {'right':1},(data)=> {
        console.log(data)
      });} 
  if (keyPressed==s){
        $.post("/rev", {'rev':1},(data)=> {
          console.log(data)
        });} 
  if (keyPressed==space){ 
      $.post("/stop", {'stop':1},(data)=> {
        console.log(data)
      });}
});


$('#forward').click(function(e) {
  $.post("/w", {'forward':1},(data)=> {
console.log(data)
  });
});


$('#left').click(function(e) {
  $.post("/a", {'left':1},(data)=> {
console.log(data)
  });
});

$('#right').click(function(e) {
  $.post("/d", {'right':1},(data)=> {
console.log(data)
  });
});

$('#rev').click(function(e) {
  $.post("/rev", {'rev':1},(data)=> {
console.log(data)
  });
});

$('#stop').click(function(e) {
  $.post("/stop", {'stop':1},(data)=> {
console.log(data)
  });
});