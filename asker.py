from flask import request

@app.router('/login, methods=['POST','GET')]
def login():
    error = None
    if request.method == 'POST'
        if valid_login(request.from['username'],
                       request.from['password']):
            return log_the_user_in(request.from['username'])
        else:
                error = 'Invalid username/password'
    #当请求形式为‘GET’或者认证失败则执行以下代码
    return render_template('login.html',error=error)