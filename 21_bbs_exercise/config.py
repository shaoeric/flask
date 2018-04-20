import os
DEBUG = True

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'bbs_exercise'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"\
    .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)

CMS_USER_ID = 'ASDSFSWWRFR'

# 发送者邮箱的服务器地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_USERNAME = '1194684253@qq.com'
MAIL_PASSWORD = 'ylypchturseafjdd'
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_DEFAULT_SENDER = '1194684253@qq.com'
# MAIL_DEBUG
