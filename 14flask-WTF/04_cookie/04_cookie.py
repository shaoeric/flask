from flask import Flask, request, Response
from cmsviews import bp

app = Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME'] = 'hy.com:5000'
# 这里需要改hosts 127.0.0.1  hy.com

@app.route('/')
def hello_world():
    resp = Response("设置cookie")
    # resp.set_cookie('username', 'zhiliao', max_age=200)  # max_age 距离当前时间的秒数
    resp.set_cookie('username', 'zhiliao', domain='.hy.xom')  # 传递domain参数 可以在子域名访问cookie信息

    return resp

@app.route('/del/')
def delete_cookie():
    resp = Response("删除cookie")
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run()
