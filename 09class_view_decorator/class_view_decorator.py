from flask import Flask, request, views
from functools import wraps
app = Flask(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username == 'eric':
            return func(*args, **kwargs)
        else:
            return '请先登陆'
    return wrapper

@app.route('/setting/')
# 视图函数装饰器，放在路由函数下面
@login_required
def settings():
    return '这是设置界面'

class ProfileView(views.View):
    # 类视图装饰器
    decorators = [login_required]
    def dispatch_request(self):
        return '这是个人中心界面'

app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
