from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def get_in():
    return render_template('hello_.html')

