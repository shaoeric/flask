import os

DEBUG = True
# SECRET_KEY = os.urandom(24)
SECRET_KEY = 'sdgastgrwaert3wqtrrasd'

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'bbs_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'ADFWFWFWF'  # 随便一个字符串 以后验证session中的cms_user_id，只需要用常量形式验证，而具体值是多少不清楚，更加安全
FRONT_USER_ID = 'SFSKLJ345315'

# 发送者邮箱的服务器地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_USERNAME = '1194684253@qq.com'
MAIL_PASSWORD = 'ylypchturseafjdd'
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_DEFAULT_SENDER = '1194684253@qq.com'
# MAIL_DEBUG

UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


# 一页10片帖子
PER_PAGE = 10
