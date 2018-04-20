from sqlalchemy import create_engine, Column, Integer, String, Float, \
    Boolean, DECIMAL, Enum, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
import enum

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

class TagEnum(enum.Enum):
    python = 'python'
    flask = 'flask'
    django = 'django'

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, autoincrement=True, primary_key=True)
    # price = Column(Float)
    # float  double类型会丢失精度，使用decimal不会丢失
    # is_delete = Column(Boolean)
    # price = Column(DECIMAL(10, 4))     # 100000.0001 最多10位， 小数点后4位
#                                          超出范围就报错
#     tag = Column(Enum("python", "flask", "django"))
#     tag = Column(Enum(TagEnum))
#     create_time = Column(Date)
    create_time = Column(DateTime)


Base.metadata.drop_all()   # 删掉当前绑定Base类的子类表
Base.metadata.create_all()

# article = Article(tag="python")
# article = Article(tag=TagEnum.python)

# from datetime import date
# article = Article(create_time=date(2017, 10, 10))

from datetime import datetime
article = Article(create_time=datetime(2011, 11, 11, 11, 11, 11))

session.add(article)
session.commit()
