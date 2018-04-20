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
    city = Column(String(50), nullable=False)
    age = Column(Integer, default=0)
    def __repr__(self):
        return "<User(username: %s)>" % self.username


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='user1', city='长沙',age=18)
# user2 = User(username='user2', city='长春', age=19)
# user3 = User(username='user3', city='杭州', age=19)
# user4 = User(username='user4', city='武汉', age=20)
# user5 = User(username='user5', city='武汉', age=20)
#
# session.add_all([user1, user2, user3, user4, user5])
# session.commit()

# 查找和user4这个人在同一个城市  并且同一年龄的人
# user = session.query(User).filter(User.username == 'user5').first()
# users = session.query(User).filter(User.city == user.city,\
#                                    User.age == user.age).all()
# print(users)   查找的太多，效率就低


# 使用subquery子查询 需要对query查到的结果定义别名.label(), 进行后续查询时，利用子查询的stmt.c.别名   c是Column的缩写
stmt = session.query(User.city.label('city'), User.age.label('age')).filter(User.username == 'user5').subquery()
result = session.query(User).filter(User.city == stmt.c.city, User.age == stmt.c.age).all()
print(result)
