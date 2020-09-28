const w = 119
const a = 97
const s = 115
const d = 100
var canvas = document.getElementById("myCanvas");
var c=document.getElementById('myCanvas');
var ctx=c.getContext('2d');
ctx.translate(100,0);
ctx.fillRect(0,0,100,50);

let rando = Math.floor(Math.random()*400)
console.log(rando)

$(document).keypress(function(e) {
  let keyPressed = e.keyCode
  // console.log(keyPressed)
  $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando },(data)=> {
    let y = data[1]
    let x = data[0]
    console.log(x,y)
    if (keyPressed == d) {
      ctx.translate(10,0)
      ctx.fillRect(0,0,100,50);
  
    }
    if (keyPressed == s) {
      ctx.translate(0,10)
      ctx.fillRect(0,0,100,50);

    }

  });
  
});


