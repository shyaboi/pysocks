from lightOnPi import lightOn, lightOff
from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

@app.route('/on', methods=['POST'])
def receive_data():
    print(request.form['lightOn'])
    lightOn()
    return "light on"

@app.route('/off', methods=['POST'])
def receive_data2():
    print(request.form['lightoff'])
    lightOff()
    return "light off"

@app.route('/')
def hello():
    return render_template('index.html')