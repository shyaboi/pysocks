from lightOnPi import lightOnS,lightOnA, lightOff
from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

@app.route('/on', methods=['POST'])
def on():
    print(request.form['lightOn'])
    lightOnS()
    lightOnA()
    return "light on"
@app.route('/a', methods=['POST'])
def on():
    print(request.form['lightOn'])
    lightOnA()
    return "light on"
@app.route('/off', methods=['POST'])
def off():
    print(request.form['lightOff'])
    lightOff()
    return "light off"

@app.route('/')
def hello():
    return render_template('index.html')