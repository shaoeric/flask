from flask import Flask, render_template, request
from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo

class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名长度必须在3到10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=6, max=10), EqualTo("password")])


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template("regist.html")
    else:
        form = RegistForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return "fail"

        # username = request.form.get("username")
        # password = request.form.get("password")
        # password_repeat = request.form.get("password_repeat")
        # if len(username)<3 or len(username)>10:
        #     return "用户名长度不正确"
        # if len(password)<6 or len(password)>10:
        #     return "密码长度不正确"
        # if password != password_repeat:
        #     return "两次密码输入不一致"

if __name__ == '__main__':
    app.run(debug=True)
