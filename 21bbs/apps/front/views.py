from flask import Blueprint, views, render_template, make_response, request, session, url_for, g, abort
from utils.captcha import Captcha
from io import BytesIO
from .forms import SigninForm, AddPostForm, AddCommentForm
from .models import FrontUser
import config
from utils import restful
from apps.models import BoardModel, PostModel, CommentModel,HighlightPostModel
from .decorators import login_required
from exts import db
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy.sql import func

bp = Blueprint("front", __name__)

@bp.route('/')
def index():
    board_id = request.args.get('bd', type=int, default=None)
    sort = request.args.get('st', type=int, default=1)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    boards = BoardModel.query.all()
    start = (page-1)*config.PER_PAGE
    end = start+config.PER_PAGE
    posts = None
    total = 0

    query_obj = None
    if sort == 1:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 2:
        # 加精的时间倒叙排列
        query_obj = db.session.query(PostModel).outerjoin(HighlightPostModel).order_by(HighlightPostModel.create_time.desc(), PostModel.create_time.desc())
    elif sort == 3:
    #     按照点赞的顺序  （点赞没做）
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 4:
    #     按照评论数量
        query_obj = db.session.query(PostModel).outerjoin(CommentModel).group_by(PostModel.id).order_by(func.count(CommentModel.id).desc(), PostModel.create_time.desc())
    if board_id:
        posts = query_obj.filter(PostModel.board_id == board_id).slice(start, end)
        total = query_obj.filter(PostModel.board_id==board_id).count()
    else:
        posts = query_obj.slice(start, end)
        total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total)
    context = {
        'boards': boards,
        'posts': posts,
        'pagination': pagination,
        'current_board': board_id,
        'current_sort': sort
    }
    return render_template('front/front_index.html', **context)

@bp.route('/p/<post_id>')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    if not post:
        abort(404)
    return render_template('front/front_pdetail.html', post=post)

@bp.route('/acomment/', methods=['POST'])
@login_required
def add_comment():
    form = AddCommentForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        post = PostModel.query.get(post_id)
        if post:
            comment = CommentModel(content=content)
            comment.post = post
            comment.author = g.front_user
            db.session.add(comment)
            db.session.commit()
            return restful.success()
        else:
            return restful.paramserror(message='没有这个帖子')
    else:
        return restful.paramserror(form.get_error())


class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')

bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))

@bp.route('/apost/', methods=['GET', 'POST'])
@login_required
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        context = {
            'boards': boards
        }
        return render_template('front/front_apost.html', **context)
    else:
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.paramserror(message='没有这个板块')
            post = PostModel(title=title, content=content)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            return restful.paramserror(form.get_error())


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to!= request.url and return_to!=url_for('front.signup'):
            return render_template('front/front_signin.html', return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.paramserror(message='手机号码或密码错误')
        return restful.paramserror(message=form.get_error())

bp.add_url_rule('/signin/', view_func=SigninView.as_view('signin'))
