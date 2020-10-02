from lightOnPi import forwardBlue,forwardRed, forwardAll, stop, rev, left, right
from flask import Flask, render_template, request, jsonify
import random, time
app = Flask(__name__)

# @app.route('/on', methods=['POST'])
# def on():
#     print(request.form['lightOn'])
#     return " all lights on"

@app.route('/w', methods=['POST'])
def forward():
    forwardAll()
    print(request.form['forward'])
    return "going forward"

@app.route('/a', methods=['POST'])
def leftTurn():
    left()
    print(request.form['left'])
    return "left turnning"

@app.route('/d', methods=['POST'])
def rightTurn():
    right()
    print(request.form['right'])
    return "right turnning"

@app.route('/rev', methods=['POST'])
def reverse():
    rev()
    print(request.form['rev'])
    return "reversing"

@app.route('/stop', methods=['POST'])
def off():
    print(request.form['stop'])
    stop()
    return "stopping"

@app.route('/')
def hello():
    return render_template('index.html')