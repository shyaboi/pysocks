from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/push', methods=['POST'])
def receive_data():
   print(request.form['keyPressed'])
   return "response from server" + request.form['keyPressed']
@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)