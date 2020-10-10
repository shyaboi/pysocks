# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
from lightOnPi import forwardBlue,forwardRed, forwardAll, stop, rev, left, right

PAGE="""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rad Mobile 2</title>
    <script
      src="https://code.jquery.com/jquery-3.5.1.js"
      integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc="
      crossorigin="anonymous"
    ></script>
</head>
<body>
   <button id="forward">Forward</button>
   <br>
   <button id="left">Left</button>
   <button id="right">Right</button>
   <br>
   <button id="rev">Reverse</button>
   <br>
   <button id="stop">Stop</button>





<center><h1>Rad Mobile 2</h1></center>
<center><img src="stream.mjpeg" width="1080" height="720"></center>
<script>const w = 119
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
});</script>
</body>

</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()
    def do_POST(self):
        if self.path == '/w':
            forwardAll()
        if self.path == '/a':
            left()
        if self.path == '/rev':
            rev()
        if self.path == '/d':
            right()
        if self.path == '/stop':
            stop()
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += " <h2> hiwrld </h2>"
            output += "</body></html>"
            self.wfile.write(output.encode(encoding = "utf_8"))
            print (output)
        except:
            pass
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

with picamera.PiCamera(resolution='1080x720', framerate=30) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    camera.start_recording(output, format='mjpeg', resize='1080x720', splitter_port=1, quality=100)
    try:
        address = ('0.0.0.0', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
