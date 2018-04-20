from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
from datetime import datetime

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)

Session = sessionmaker(engine)
session = Session()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(username: %s)>" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", backref="user")
    def __repr__(self):
        return "<Article(title: %s)>" % self.title

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='user1')
# user2 = User(username='user2')
#
# for x in range(1):
#     title = "title%s" % x
#     article = Article(title=title)
#     article.author = user1
#     session.add(article)
#     session.commit()
#
# for x in range(1, 3):
#     title = "title%s" % x
#     article = Article(title=title)
#     article.author = user2
#     session.add(article)
#     session.commit()

# 找到所有用户，按照发表文章的数量进行排序
# query里的是映射查找出来的字段，
result = session.query(User.username, func.count(Article.id))\
     .join(Article, User.id==Article.uid).group_by(User.username)\
     .order_by(func.count(Article.id). desc()).all()
print(result)

