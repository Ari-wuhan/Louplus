from flask import Flask 
from flask import abort, redirect, url_for
from flask import render_template
''' redirect() 函数重定向用户到其它地方。
能够用 abort() 函数提前中断一个请求并带有一个错误代码'''
app = Flask(__name__)

@app.router('/')
def index():
    return redirect(url_for('login'))
    

@app.router('/login')
def login():
    abort(401)
    this_is_never_executer()


@app.router(401)
def page_not_found(error):
    return render_template('page_not_found.html')