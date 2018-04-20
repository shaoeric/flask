from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Table
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

#  多对多的实现，，多对一  与 一对多的复合关系（笛卡儿积）
#  新建一个中间表article_tag#
#  以两个外键复合起来作为中间表的主键#
article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True)
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    #                       secondary指代多对多关系，连接中间表
    tags = relationship("Tag", backref="articles", secondary=article_tag)

    def __repr__(self):
        return "Article%s" % self.title

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return "Tag%s" % self.name
# 步骤：
# 1.先把两个需要多对多的模型定义出来
# 2.使用Table定义一个中间表 中间表一般包括两个模型的外键字段就可以 并且让他们两个作为一个
# 复合主键
# 3.定义relationship 绑定三者的关系 传入secondary中间表#

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(title='article1')
# article2 = Article(title='article2')
#
# tag1 = Tag(name='tag1')
# tag2 = Tag(name='tag2')
#
# article1.tags.append(tag1)
# article1.tags.append(tag2)
# article2.tags.append(tag1)
#
# session.add(article1)
# session.add(article2)
# session.commit()


article1 = session.query(Article).first()
print(article1.tags)