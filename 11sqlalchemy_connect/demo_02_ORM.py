from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
# 继承基类 创建一张person表
class Person(Base):
    __tablename__ = 'person'   # 表名为person
    # 创建类属性->表的字段名
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    # 将创建好的orm模型映射到数据库中
Base.metadata.create_all()
