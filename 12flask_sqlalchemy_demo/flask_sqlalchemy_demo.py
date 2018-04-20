from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Users(username:%s)>' % self.username
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User", backref='articles')

# db.drop_all()
# db.create_all()

# user = User(username='张三')
# article = Article(title='title1')
# article.author = user
# db.session.add(article)
# db.session.commit()

# 简单查询可以直接使用模型User.query  ，若是复杂查询 join等 ，还得是db.session查询
# users = User.query.order_by(User.id.desc()).all()
# print(users)

# 更新
# user = User.query.filter(User.username == '张三').first()
# user.username = '张三1'
# db.session.commit()

# 删除
# user = User.query.filter(User.username == '张三1').first()
# db.session.delete(user)
# db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
