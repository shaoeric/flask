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

 # 使用alembic映射到数据库当中
# 初始化alembic仓库 在终端中 cd到项目目录中 执行命令alembic init alembic，创建一个名叫alembic的仓库,        然后在生成的项目中alembic.ini修改sqlalchemy.url,,                 在env.py中 import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# import models，改target_metadata = models.Base.metadata

# 以后更新数据库只执行下面两条
# 终端中输入指令   alembic revision --autogenerate -m "first commit（此处是版本号）"生成迁移脚本
# 终端输入命令  alembic upgrade head 更新数据库