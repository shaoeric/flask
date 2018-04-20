from flask import Flask
import config
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
from exts import db, mail
from flask_wtf import CSRFProtect
from apps.ueditor import bp as ueditor_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # 前台后台公共三个蓝图
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(ueditor_bp)
    db.init_app(app)
    mail.init_app(app)
    CSRFProtect(app)
    return app



if __name__ == '__main__':
    create_app().run()
