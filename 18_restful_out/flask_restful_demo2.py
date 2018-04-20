from flask import Flask
import config
from exts import db
from models import *
from articleviews import article_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(article_bp)


# 定义一个Article模型, 类视图可以通过get返回模型
# class Article(object):
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
# article = Article(title='abc', content='xxx')
#
# class ArticleView(Resource):
#
#     resource_fields = {
#         'title': fields.String,
#         'content': fields.String
#     }
#     @marshal_with(resource_fields, envelope='data')
#     # envelope是可选参数, 会把值填到返回值的最前端,{"data": {"title": "xxx", "content": "xxx"}}
#     # def get(self):
#     #     return {'title': 'xxx', 'content': 'xxx'}
#     def get(self):
#         return article
#
# api.add_resource(ArticleView, '/article/', endpoint='article')


@app.route('/')
def hello_world():
    user = User(username='zhi', email='xxx@qq.com')
    article = Article(title='abc', content='123')
    article.author = user
    tag1 = Tag(name='python')
    tag2 = Tag(name='java')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()

    return 'Hello World!'


# 1.flask-restful结合蓝图  articleviews.py
# 若有多个蓝图, 就每个蓝图里都定义api=Api(blue_print)

# 2.flask-restful渲染模板



if __name__ == '__main__':
    app.run()
