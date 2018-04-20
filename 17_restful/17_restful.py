from flask import Flask, url_for
from flask_restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
api = Api(app)

# class Login_view(Resource):
#     def post(self):
#         return {'username': 'zhi'}
# api.add_resource(Login_view, '/login/', endpoint='login')
#
# with app.test_request_context():
#     print(url_for('login'))


# url带有参数形式
# class Login_view(Resource):
#     def post(self, username=None):
#         return {'username': 'zhi'}
# #     *urls可以是一个  也可以是多个， login需要带参数，regist不需要参数，
# #      url带参数是post请求要有参数, 没有参数则用None值
# api.add_resource(Login_view, '/login/<username>', '/regist/', endpoint='login')


class Login_view(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        # 当出现错误的时候, 返回help参数值
        parser.add_argument('username', type=str, help='用户名验证错误', required=True)
        parser.add_argument('password', type=str, help='密码错误')
        parser.add_argument('age', type=int, help='年龄验证错误')
        parser.add_argument('gender', type=str, choices=['male', 'female', 'secret'])
        # type可以是用内置形式,如url, 正则, date
        parser.add_argument('home_page', type=inputs.url, help='个人主页链接验证错误')
        parser.add_argument('telephone', type=inputs.regex(r'1[3578]\d{9}'))
        parser.add_argument('birthday', type=inputs.date)
        args = parser.parse_args()
        print(args)
        return {'username': 'zhi'}

api.add_resource(Login_view, '/login/')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
