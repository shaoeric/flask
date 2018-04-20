from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# ext实例化db后,分成两路  -> app进行初始化绑定
#                         -> models定义模型数据表
