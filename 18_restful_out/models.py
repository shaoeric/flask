from exts import db


# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

#    文章标签多对多, 定义中间表
article_tag_table = db.Table('article_tag',
        db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

# 文章
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship("User", backref='articles')
    tags = db.relationship("Tag", secondary=article_tag_table, backref='articles')

# 标签, 与文章多对多
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
