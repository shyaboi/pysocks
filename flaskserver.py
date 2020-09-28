from lightOnPi import lightOnS,lightOnA, lightOff
from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

@app.route('/on', methods=['POST'])
def on():
    print(request.form['lightOn'])
    lightOnS()
    lightOnA()
    return " all lights on"

@app.route('/w', methods=['POST'])
def leftOn():
    print(request.form['lightOn'])
    lightOnA()
    return "light a on"
@app.route('/s', methods=['POST'])
def backOn():
    print(request.form['lightOn'])
    lightOnS()
    return "light s on"

@app.route('/off', methods=['POST'])
def off():
    print(request.form['lightOff'])
    lightOff()
    return "light off"

@app.route('/')
def hello():
    return render_template('index.html')