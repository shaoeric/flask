from flask import Flask, views, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

class LoginView(views.MethodView):
    def __render(self, error=None):
        return render_template('login.html', error=error)

    def get(self):
        return self.__render()
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'eric' and password == '123':
            return '登录成功'
        else:
            return self.__render(error='登录失败')

app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
if __name__ == '__main__':
    app.run()
