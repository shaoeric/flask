from flask import Blueprint, render_template, make_response
from flask_restful import Api, Resource, fields, marshal_with
from models import Article


article_bp = Blueprint('article', __name__, url_prefix='/article')
api = Api(article_bp)

class ArticleView(Resource):

    resource_fields = {
        'title': fields.String(attribute='article_title'),   # 重命名属性
        "content": fields.String,
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String
        }),
        'tags': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String
        })),
        'read_count': fields.Integer(default=80)   # 默认值
    }
    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article

api.add_resource(ArticleView, '/<article_id>/', endpoint='aricle')



# 渲染模板
# 不能直接用render_template渲染,会直接以json形式返回网页代码
# 通过给api添加装饰器,以html形式返回 一个response的对象
@api.representation('text/html')
def output_html(data, code, headers):
    response = make_response(data)
    return response

class ListView(Resource):
    def get(self):
        return render_template("index.html")
api.add_resource(ListView, '/list/', endpoint='list')