from flask import Blueprint

news_bp = Blueprint('news', __name__)

@news_bp.route('/news/')
def news():
    return '新闻页面'

@news_bp.route('/detail/')
def news_detail():
    return '新闻详情'