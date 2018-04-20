from flask import Flask, url_for, render_template
from blue_prints.users import user_bp
from blue_prints.news import news_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)
# 实现对大项目的分层解耦
# 用户模块
# 新闻模块
# 电影模块。。。
@app.route('/')
def hello_world():
    print(url_for('user.profile'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
