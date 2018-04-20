from flask import Blueprint, request

bp = Blueprint('cms', __name__, subdomain='cms')   # 添加子域名

@bp.route('/')
def index():
    username = request.cookies.get('username')
    return username or '没有获取到cookie'
