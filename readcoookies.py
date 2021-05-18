from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    #这里引用cookies字典的键值是对使用cookies.get(key)
    #而不是cookies[key],这是防止该字典不存在时报错'keyerror'
    