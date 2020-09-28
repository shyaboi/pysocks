from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

@app.route('/push', methods=['POST'])
def receive_data():
   print("player: " + request.form['playerNum'], "pressed the "+ request.form['keyPressed']+" key")
   playerNum = request.form['playerNum']
   keypressed = request.form['keyPressed']
   rand1 = random.randint(1, 401)
   rand2 = random.randint(1, 301)
   x=str(rand1)
   y=str(rand2)
   player = jsonify(x,y)
# f"player: { request.form['playerNum']} pressed the {request.form['keyPressed']} key"

   return player
@app.route('/')
def hello():
    return render_template('index.html')