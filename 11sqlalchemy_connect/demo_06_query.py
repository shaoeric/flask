from sqlalchemy import create_engine, Column, Integer, Float, String, func
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

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return '<Article(title:%s)>' % self.title
# Base.metadata.drop_all()   # 删掉当前绑定Base类的子类表
# Base.metadata.create_all()

# import random
# for x in range(6):
#     article = Article(title='title%s'%x, price=random.randint(50, 100))
#     session.add(article)
# session.commit()

# 查询模型属性
articles = session.query(Article.title, Article.price).all()
print(articles)

# 聚合函数
result = session.query(func.count(Article.id)).first()    # 查询共有多少数据
print(result)

result = session.query(func.avg(Article.price)).first()    # 查询price属性平均值
print(result)