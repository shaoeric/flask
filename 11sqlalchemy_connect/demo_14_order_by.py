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

    # 第三种方式 默认指定倒叙排序
    __mapper_args__ = {
        'order_by': create_time.desc()
    }

    def __repr__(self):
        return '<Article:title:%s, create_time:%s>' % (self.title, self.create_time)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# article = Article(title='title3')
# session.add(article)
# session.commit()

# 1.正序排序，最后发布的在最后
# articles = session.query(Article).order_by(Article.create_time).all()

# 2.倒叙排序
# articles = session.query(Article).order_by(Article.create_time.desc()).all()

# 3.__mapper_args__
articles = session.query(Article).all()
print(articles)