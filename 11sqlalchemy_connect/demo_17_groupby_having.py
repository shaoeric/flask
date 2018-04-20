from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey, func
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
    age = Column(Integer,default=0)
    gender = Column(Enum("male", "female", "secret"), default="male")

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='wang', age=17, gender='male')
# user2 = User(username='wang1', age=16, gender='male')
# user3 = User(username='wang2', age=18, gender='female')
# user4 = User(username='wang3', age=18, gender='female')
# session.add_all([user1, user2, user3, user4])
# session.commit()

# 每个年龄的人数 group_by
result = session.query(User.age, func.count(User.id)).group_by(User.age).all()
print(result)

# 未成年人的人数 having  实际上就是filter的功能
result = session.query(User.age, func.count(User.id)).group_by(User.age)\
    .having(User.age<18).all()
print(result)