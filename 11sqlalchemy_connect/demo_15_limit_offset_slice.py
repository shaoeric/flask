from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
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

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return "<Article(title: %s)>" % self.title
# Base.metadata.drop_all()
# Base.metadata.create_all()

# for x in range(100):
#     title = "title%s" % x
#     article = Article(title=title)
#     session.add(article)
#     session.commit()

# 从第5条开始，共10条数据  5~14
# articles = session.query(Article).offset(5).limit(10).all()
# print(articles)

# 94~85  共10条数据
# articles = session.query(Article).order_by(Article.id.desc()).offset(5).limit(10).all()
# print(articles)

# 指定从哪开始 到哪结束 92~90
articles = session.query(Article).order_by(Article.id.desc()).slice(7, 10).all()
print(articles)
