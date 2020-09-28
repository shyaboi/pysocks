const w = 119
const a = 97
const s = 115
const d = 100

$(document).keypress(function(e) {
  let keyPressed = e.keyCode
  console.log(keyPressed)
  $.post("/push", {'keyPressed':keyPressed},(data)=> {
  console.log(data)
  });
  
});
