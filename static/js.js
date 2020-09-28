const w = 119
const a = 97
const s = 115
const d = 10
const l = 108
var canvas = document.getElementById("myCanvas");
var c=document.getElementById('myCanvas');
var ctx=c.getContext('2d');

let rando = Math.floor(Math.random()*400)
let x=rando,y=rando
var loc = (x,y)=> {return [x,y]}
ctx.translate(rando,rando)
$('#butt').keypress(function(e) {
  let keyPressed = e.keyCode
  console.log(keyPressed)
  // $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando, 'playerLocX':rando, 'playerLocY':rando  },(data)=> {
  $.post("/push", {'lightOn':1},(data)=> {
console.log(data)
  //   ctx.clearRect(0, 0, canvas.width, canvas.height);
 
  //   if (keyPressed == w) {
  //     ctx.translate(0,-1)
  //     y=y-1
  //     ctx.fillRect(0,0,50,10);
  //     $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando, 'playerLocX':x, 'playerLocY':y },(data)=> {console.log(data)})
  //   }
  //   if (keyPressed == d) {
  //     ctx.translate(1,0)
  //     x=x+1
  //     ctx.fillRect(0,0,50,10);
  //     $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando, 'playerLocX':x, 'playerLocY':y },(data)=> {console.log(data)})
  //   }

  //   if (keyPressed == s) {
  //     ctx.translate(0,1)
  //     y=y+1
  //     $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando, 'playerLocX':x, 'playerLocY':y },(data)=> {console.log(data)})
  //     ctx.fillRect(0,0,50,10);
  //   }
   
  //   if (keyPressed == a) {
  //     ctx.translate(-1,0)
  //     x=x-1
  //     ctx.fillRect(0,0,50,10);
  //     $.post("/push", {'keyPressed':keyPressed, 'playerNum':rando, 'playerLocX':x, 'playerLocY':y },(data)=> {console.log(data)})
  //   }

  });
  
});


