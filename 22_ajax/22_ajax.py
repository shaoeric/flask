from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '首页'

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'eric' and password == '111':
            return redirect(url_for('index'))
        else:
            return '用户名或密码错误'

if __name__ == '__main__':
    app.run()
