from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

@app.route('/push', methods=['POST'])
def receive_data():
   playerNum = request.form['playerNum']
   keypressed = request.form['keyPressed']
   playerLocX = request.form['playerLocX']
   playerLocY = request.form['playerLocY']
   if playerNum != playerNum:
       print('playa2 in the houssseeeeeeeee')
       if playerLocX == playerLocX:
            print('booooooooooooooooooooooooooooooooom')
   print(f'Player# {playerNum} currently at [{playerLocX}, {playerLocY}]')
   return jsonify(playerNum,playerLocX,playerLocY)
@app.route('/')
def hello():
    return render_template('index.html')