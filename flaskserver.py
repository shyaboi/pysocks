from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/push', methods=['POST'])
def receive_data():
   print("player: " + request.form['playerNum'], "pressed"+ request.form['keyPressed']+"key")
   return "player: " + request.form['playerNum'], "pressed"+ request.form['keyPressed']+"key"
@app.route('/')
def hello():
    return render_template('index.html')