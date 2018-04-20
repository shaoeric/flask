from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

engine = create_engine(DB_URI)
# 判断连接是否成功

# 创建一个orm基类
Base = declarative_base(engine)

# 创建会话
Session = sessionmaker(engine)
session = Session()

# 继承基类 创建一张person表
class Person(Base):
    __tablename__ = 'person'   # 表名为person
    # 创建类属性->表的字段名
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    # 将创建好的orm模型映射到数据库中
# Base.metadata.create_all()

def add_data():
    p = Person(name='eric', age=19)   # 实例化一个对象/一条数据
    p2 = Person(name='eric', age=18)   # 实例化一个对象/一条数据
    # session.add(p)
    session.add_all([p, p2])
    session.commit()
    session.close()

def del_data():
    person = session.query(Person).first()
    session.delete(person)
    session.commit()

def update_data():
    person = session.query(Person).first()
    person.name = 'Eric'
    session.commit()

def search_data():
    # all_person = session.query(Person).all()  # 查找全部数据
    # all_person = session.query(Person).filter_by(id=1).all()
    all_person = session.query(Person).filter(Person.id == 2).all()
    print(all_person)

# add_data()
# search_data()
# update_data()
del_data()