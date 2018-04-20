from flask import Flask, views, jsonify, render_template

app = Flask(__name__)

class JsonView(views.View):
    def get_data(self):
        raise NotImplementedError
    def dispatch_request(self):
        return jsonify(self.get_data())

class ListView(JsonView):
    def get_data(self):
        return {'username': 'eric', 'password': '1111111'}

# 对类视图添加视图函数，as.view是将类视图转化为函数的方法，实际上是返回了dispatch_request的方法
app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))


class Ads(views.View):
    def __init__(self):
        super(Ads, self).__init__()
        self.context = {
            'ads': '今年过节不收礼',
        }

class LoginView(Ads):
    def dispatch_request(self):
        self.context.update({'username': 'eric'})
        return render_template('login.html', **self.context)

class RegistView(Ads):
    def dispatch_request(self):
        return render_template('regist.html', **self.context)

app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
