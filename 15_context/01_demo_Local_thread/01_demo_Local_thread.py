from flask import Flask, request, current_app, url_for, g, session, render_template
from werkzeug.local import Local
from utils import log_a, log_b
import os

# 只要绑定在Local对象上的属性
# 在每个线程中都是隔离的
# 为了避免在多用户同时访问时，request互相产生影响，用线程相互隔离
# 详细查看text_demo文件
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 手动将app上下文推入栈
app_context = app.app_context()  # 创建app上下文
app_context.push()
# print(current_app.name)
@app.route('/')
def hello_world():
    # print(current_app.name)  # 只能在视图函数内打印当前应用的名字
    # 因为在通过url形式访问视图函数，会将上下文推入栈中，可以访问，否则放在视图函数外面则不会进入栈中，则访问不到，就会报错。可以手动将上下文推入
    # print(url_for("my_list"))

    if hasattr(g, 'user'):   # before_request 每次请求之前执行，避免每次都要访问数据库
        print(g.user)
    return render_template("index.html")

@app.route('/list/')
def my_list():
    # username = request.args.get('username')
    # #  g对象  global缩写
    # g.username = username
    # utils文件调用
    # log_a()
    # log_a()

    print(g.user)  # 在没有g.user变量情况下，让服务器发动errorhandler处理

    session['user_id'] = 1
    return 'mylist'

# with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会自动先推入一个应用上下文到栈中
    # print(url_for("my_list"))


# 钩子函数，在普通函数之前调用
# @app.before_first_request   #  第一次请求之前就执行, 只执行一次
# def first_request():
#     print('before_first_request')


# @app.before_request
# def before_request():
#     # print("在视图函数执行之前执行")   # 每次请求都会执行, 避免每次都要在数据库操作
#     user_id = session.get('user_id')
#     if user_id:
#         g.user = 'zhi'

# @app.context_processor
# # 自动将字典参数渲染到模板当中，避免每次都要传参.  而且必须要返回一个字典，否则会有问题
# def context_processor():
#     return {"current_user": "zhi"}


@app.errorhandler(500)
def service_error(error):
    return "您刷新的太频繁", 500    # 此处500是让状态码显示真实值，有利于seo优化

if __name__ == '__main__':
    app.run()
