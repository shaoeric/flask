from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
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

    # articles = relationship("Article")  # 找到所有文章   一对多
#        Article表里author添加backref 即可代表两表互相关联
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    # 用户表的id作为关联
    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))

    # 通过relationship拿到User表下的所有属性
    author = relationship("User", backref='articles')
                               # 实际上articles属性是属于User的，User可以
    #                        通过articles属性访问Article的属性

    def __repr__(self):
        return "<Article(title:%s, content=%s)>" % (self.title, self.content)

# 基于demo08的代码来的，有两个表user和article 存在一个外键id->uid
# article = session.query(Article).first()
# uid = article.uid
# print(uid)
# user = session.query(User).filter_by(id=uid).first().username
# print(user)   这样做太麻烦 应该使用orm relationship


# 使用relationship后
# article = session.query(Article).first()
# print(article.author.username)

user = session.query(User).first()
print(user.articles)


# 一对多的添加
# user = User(username='Eric')
# article1 = Article(title='abc', content='123')
# article2 = Article(title='addd', content='1144')
# # user.articles   是list类型数据
# user.articles.append(article1)
# user.articles.append(article2)
# # 直接添加user 会自动添加article，级联操作
# session.add(user)
# session.commit()


# 反向添加
user = User(username='Eric')
article1 = Article(title='abc', content='123')
article1.author = user
session.add(article1)
session.commit()
