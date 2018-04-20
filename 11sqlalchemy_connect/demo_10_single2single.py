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

# user/article  父表/子表
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    # 让uselist=False，关掉一对多的模式,
    # 做了优化   将这一步放在UserExtend中合并
    # extend = relationship('UserExtend', uselist=False)

    def __repr__(self):
        return '<User(username:%s)>' % self.username

# 对于user的一些不常用属性 比如籍贯 毕业院校，可以与User形成一对一关系
class UserExtend(Base):
    __tablename__ = 'userextend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref('extend', uselist=False))    # 反向参考添加extend属性，关闭一对多模式

Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username='eric')
extend = UserExtend(school='zhiliaoketang')
user.extend = extend
session.add(user)
session.commit()
