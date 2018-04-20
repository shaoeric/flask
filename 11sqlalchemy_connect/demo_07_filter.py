from sqlalchemy import create_engine, Column, Integer, Float, String, or_
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
    content = Column(String(100))
    def __repr__(self):
        return '<Article(title:%s)>' % self.title

# session.query(Article).filter(Article.id == 1)
# session.query(Article).filter_by(id=1)   功能有限，所以很少用filter_by方法

# equal
# result = session.query(Article).filter(Article.id == 1).first()
# print(result)

# not equal
# result = session.query(Article).filter(Article.title != 'title0').all()
# print(result)

# like  模糊搜索     .ilike()不区分大小写
#  result = session.query(Article).filter(Article.title.like('title%')).all()
# print(result)

# in
# result = session.query(Article).filter(Article.title.in_(['title1', 'title2'])).all()
# print(result)

# not in
# result = session.query(Article).filter(Article.title.notin_(['title1', 'title2'])).all()
# print(result)

# is_null
# result = session.query(Article).filter(Article.content==None).all()
# print(result)

# result = session.query(Article).filter(Article.content!=None).all()
# print(result)

# and
# result = session.query(Article).filter(Article.title=='abc', \
#                                     Article.content=='abc').all()
# print(result)

#  or
result = session.query(Article).filter(or_(Article.content=='abc',\
                                           Article.title=='abc')).all()
print(result)
