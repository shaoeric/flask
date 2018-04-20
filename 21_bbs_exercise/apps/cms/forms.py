from wtforms import Form, StringField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
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
    newpwd2 = StringField(validators=[EqualTo('newpwd')])

class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    captcha = StringField(validators=[Length(6, 6, message='请输入6位验证码')])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_cache = cache.get(email)
        if not captcha_cache or captcha_cache.lower() != captcha.lower():
            raise ValidationError('邮箱验证码不正确')

    def validate_email(self, field):
        email = field.data
        user = g.cms_user
        if email == user.email:
            raise ValidationError('不能修改为相同的邮箱')
