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

    author = relationship("User", backref=backref("articles", cascade="save-update, delete,\
                        delete-orphan"))
#     cascade默认是save-update， 若设为""， 则user不会添加数据，uid为null
# cascade中不设置delete项，在后续删除子表数据时，只删除子表内容
# 设置了delete，删除时，父子表对应数据都删除
# 设置了delete-orphan时， 子数据成了孤儿数据，即uid为null时， 会删除整条数据,只能用于一对多#
# 设置all 是除delete-orphan以外的所有的缩写

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='eric')
# article = Article(title='title1')
# article.author = user
# session.add(article)
# session.commit()

# article = session.query(Article).first()
# session.delete(article)
# session.commit()


# 对user表删除数据也是一样 ，设置cascade=delete项，
# 则级联删除， 否则会将uid保存为null#
# user = session.query(User).first()
# session.delete(user)
# session.commit()

# 开启delete-orphan，将user的article设置为空，则user下的文章都被删除
user = session.query(User).first()
user.articles = []
session.commit()
