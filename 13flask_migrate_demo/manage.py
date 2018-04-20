from flask_script import Manager
from flask_migrate_demo import app
from flask_migrate import Migrate, MigrateCommand
from ext import db
from models import User  # 必须要导入，不导入不能生成迁移脚本

# flask-scrip和flask-migrate结合
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)
#
# cmd运行命令
# 初始化迁移文件python manage.py db init
# 生成迁移脚本python manage.py db migrate
# 更新脚本python manage.py db upgrade#
#
if __name__ == '__main__':
    manager.run()
