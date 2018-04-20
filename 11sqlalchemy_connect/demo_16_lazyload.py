from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref

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

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))

    author = relationship("User", backref=backref("articles", lazy='dynamic'))
#                定义lazy为动态，将user.articles  (List)转换为query对象，可以进行filter处理
    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='eric')
# for x in range(100):
#     article = Article(title='title%s' % x)
#     article.author = user
#     session.add(article)
#     session.commit()

user = session.query(User).first()
# user.articles是一个AppendQuery对象,可以filter过滤， 也可以append
print(user.articles.filter(Article.id > 50).all())

# article = Article(title='title100')
# user.articles.append(article)
# session.commit()