from sqlalchemy import Column,String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'alembic_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    age = Column(Integer, default=0)


# 终端中alembic current指令 显示当前版本
#       alembic heads指令  显示脚本指向的版本
#       alembic head指令  显示最新的版本
#       alembic history指令 显示历史所有版本
