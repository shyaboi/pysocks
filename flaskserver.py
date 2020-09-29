from lightOnPi import forwardBlue,forwardRed, forwardAll, stop
from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

@app.route('/on', methods=['POST'])
def on():
    print(request.form['lightOn'])
    return " all lights on"

@app.route('/w', methods=['POST'])
def leftOn():
    forwardAll()
    print(request.form['forward'])
    return "light a on"

@app.route('/a', methods=['POST'])
def backOn():
    print(request.form['left'])
    return "light s on"

@app.route('/off', methods=['POST'])
def off():
    print(request.form['lightOff'])
    stop()
    return "light off"

@app.route('/')
def hello():
    return render_template('index.html')