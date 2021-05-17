#到入类Flask,该类的实例化将是WSGI应用
from flask import Flask



#创建该类的实例，第一个参数是应用 
#的模块或包的名称，这样Flask才会知道去哪找
app = Flask(__name__)


#使用装饰器告诉Flask那个URL可以触发我们的函数



'''定义一个函数，该函数名用来给特定函数
生成URLs，并返回我们想要显示在用户浏览器上的信息'''
@app.route('/')
def index():    #如果访问根目录'/'，返回Index Page
    return 'Index Page'

#如果访问'/hello',返回Hello,World!
def hello():
        return 'Hello, World!'
    

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/ 之后的路径名
    return 'Subpath {}'.format(subpath)

@app.route('/projects/')
     #规范的 URL 指向 projects 尾端有一个斜线 / 
     # 访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去
     # 此时如果访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'