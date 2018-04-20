from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)   # 使用session要进行加密 此处24位
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)   # 设置session有效期2小时，默认为31天

# session相当于一个字典类型

@app.route('/')
def hello_world():
    session['username'] = 'user'
    session['user_id'] = '123'
    # 设置过期时间  为持久 默认保存31天
    session.permanent = True
    return 'Hello World!'

@app.route('/get_session/')
def get_session():
    username = session.get('username')
    user_id = session.get('user_id')
    return username or '没有session'

@app.route('/delete/')
def delete():
    # 删除一个session
    # session.pop('username')
    # return '删除成功'

    session.clear()
    return '删除全部'

if __name__ == '__main__':
    app.run()
