from flask import Flask, request, g, template_rendered, got_request_exception, render_template
from blinker import Namespace
from signals import login_signal
# Namespace 命名空间
# 1定义信号
# namespace = Namespace()
# fire_signal = namespace.signal('fire')
# # 2监听信号
# def fire_bullet(sender):
#     print(sender)
#     print("start fire bullet")
# fire_signal.connect(fire_bullet)
# # 3 发送信号
# fire_signal.send()

# 定义一个登录的信号，以后用户登录进来以后就发送一个登录信号，然后能够监听这个信号，在监听到这个信号之后 就记录当前这个用户登陆的信息。用信号的方式记录用户的登录信息

app = Flask(__name__)

# def template_rendered_func(sender, template, context):
#     print(sender)
#     print(template)
#     print(context)
# template_rendered.connect(template_rendered_func)


def request_exception_fun(sender,exception):
   print(exception)
got_request_exception.connect(request_exception_fun)

@app.route('/')
def hello_world():
    # a = 1/0
    return render_template("index.html")

@app.route('/login/')
def login():
    username = request.args.get('username')
    if username:
        g.username = username
        login_signal.send()    # 这里用g对象传参
        return "登录成功"
    else:
        return "请输入用户名"

if __name__ == '__main__':
    app.run(debug=True)
