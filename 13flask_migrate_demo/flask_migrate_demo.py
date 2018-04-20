from flask import Flask
from ext import db
import config
# from models import User 这里循环引用会报错 不能直接导入，所以需要新建第三方文件ext，由ext
from models import User  # 添加了ext第三方文件后 导不导入无所谓
# 提供db给models  models提供模型给app

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)   # db绑定app， app可以访问models，也可以连接config配置


@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
