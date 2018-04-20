from flask import Blueprint, views, render_template, request, session, redirect, url_for, g, jsonify
from .forms import LoginForm, ResetpwdForm, ResetEmailForm
from .models import CMSUser, CMSPermission
from .decorators import login_required, permission_required
import config
from exts import db, mail
from flask_mail import Message
from utils import restful, cache
import string
import random

bp = Blueprint("cms", __name__, url_prefix="/cms")

@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')

@bp.route('/logout/')    # 注销
@login_required
def logout():
    session.clear()
    return redirect(url_for('cms.login'))

@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

@bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get('email')
    if not email:
        return restful.paramserror('请传递邮箱参数')
    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    captcha = "".join(random.sample(source, 6))
    message = Message('python论坛', recipients=[email], body="您的验证码是%s" % captcha)
    try:
        mail.send(message)
    except:
        return restful.servererror()

    cache.set(email, captcha)
    return restful.success()

# 邮件测试
# @bp.route('/email/')
# def email():
#     message = Message('测试', recipients=['1194684253@qq.com'], body='测试')
#     mail.send(message)
#     return 'success'

class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template("cms/cms_login.html", message=message)
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='用户名或密码错误')
        else:
            message = form.errors.popitem()[1][0]
            return self.get(message=message)

bp.add_url_rule("/login/", view_func=LoginView.as_view('login'))

class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')
    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success()
            else:
                return restful.paramserror('旧密码错误')
        else:
            return restful.paramserror(form.get_error())

bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))

class ResetEmailView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetemail.html')
    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.paramserror(form.get_error())


bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))


@bp.route('/posts/')
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')

@bp.route('/comments/')
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')

@bp.route('/boards/')
@login_required
@permission_required(CMSPermission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')

@bp.route('/fusers/')
@login_required
@permission_required(CMSPermission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')

@bp.route('/cusers/')
@login_required
@permission_required(CMSPermission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')

@bp.route('/croles/')
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')
