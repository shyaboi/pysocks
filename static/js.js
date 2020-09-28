const w = 119
const a = 97
const s = 115
const d = 100
let rando = Math.floor(Math.random()*1000)
console.log(rando)
$(document).keypress(function(e) {
  let keyPressed = e.keyCode
  // console.log(keyPressed)
  $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando },(data)=> {
  console.log(data)
  });
  
});
