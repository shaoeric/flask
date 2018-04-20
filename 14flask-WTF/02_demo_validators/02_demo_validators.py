from flask import Flask, request, render_template
from forms import RegistForm, LoginForm, SettingForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return "fail"

# from uuid import uuid4
# print(uuid4())   # 输出一个uuid

@app.route("/setting/", methods=['GET', 'POST'])
def setting():
    if request.method == 'GET':
        form = SettingForm()
        return  render_template("setting.html", form=form)
    else:
        form = SettingForm(request.form)
        pass

if __name__ == '__main__':
    app.run()
