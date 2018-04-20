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
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    #                                            要开启uid不能为空，
    #                                  orm删除数据会无视sql的的外键约束，
    #
    author = relationship("User", backref='articles')

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='eric')
# article = Article(title='hello')
# article.author = user
# session.add(article)
# session.commit()

user = session.query(User).first()
session.delete(user)
session.commit()
# 开启不能为null  删除父表会报错，