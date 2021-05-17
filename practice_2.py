from flask import Flask

app = Flask(__name__)

@app.route('/sum/<int:a>/<int:b>/')
def get_sum(a,b):
    return '{0} + {1} = {2}'.format(a,b,a+b)