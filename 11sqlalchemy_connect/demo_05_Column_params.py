from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
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
    read_count = Column(Integer, default=0)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, default=datetime.now())
    # telephone = Column(String(11), unique=True)  # 唯一， 默认是False
    update_time = Column(DateTime, onupdate=datetime.now(), default=datetime.now())
#                                  数据更新的时候会调用这个参数，更新数据，，第一次会用默认值

# Base.metadata.drop_all()   # 删掉当前绑定Base类的子类表
# Base.metadata.create_all()
#
# article = Article(title='abc')
# session.add(article)
# session.commit()

article = session.query(Article).first()
article.title = '123'
session.commit()