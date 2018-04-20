from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
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
Base = declarative_base(engine)

Session = sessionmaker(engine)
session = Session()

# user/article  父表/子表
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    # 用户表的id作为关联
    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))
#                                               在User表中删掉数据时，对Article表进行的操作
#                                                RESTRICT/NO ACTION表示不删除，
#                                                CASCADE表示级联删除
#                                                SET NULL表示设置为空   #
Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username='eric')
session.add(user)
session.commit()

article = Article(title='abc', content='123', uid=1)
session.add(article)
session.commit()