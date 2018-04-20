from wtforms import Form, StringField, IntegerField, ValidationError
from wtforms.validators import Email, InputRequired, Length, EqualTo
from apps.forms import BaseForm
from utils import cache
from flask import g

class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(3, 20, message='密码长度3到20位')])
    remember = IntegerField()

class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(3, 20, message='密码长度3到20位')])
    newpwd = StringField(validators=[Length(3, 20, message='密码长度3到20位')])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message='必须与新密码保持一致')])

class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    captcha = StringField(validators=[Length(6, 6, message="请输入6位验证码")])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_cache = cache.get(email)
        if not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise ValidationError('邮箱验证码错误')

    def validate_email(self, field):
        email = field.data
        user = g.cms_user
        if user.email == email:
            raise ValidationError('不能修改为相同的邮箱')

class AddBannerForm(BaseForm):
    name = StringField(validators=[InputRequired(message='请输入轮播图名称')])
    image_url = StringField(validators=[InputRequired(message='请输入轮播图链接')])
    link_url = StringField(validators=[InputRequired(message='请输入轮播图跳转链接')])
    priority = IntegerField(validators=[InputRequired(message='请输入轮播图优先级')])

class UpdateBannerForm(AddBannerForm):
    banner_id = IntegerField(validators=[InputRequired(message='请输入轮播图的id')])

class AddBoardForm(BaseForm):
    name = StringField(validators=[InputRequired(message='请输入板块名称')])

class UpdateBoard(AddBoardForm):
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id')])
