from apps.forms import BaseForm
from wtforms import StringField, IntegerField
from wtforms.validators import Regexp, InputRequired


class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r"1[345789]\d{9}", message='请输入正确格式的手机号码！')])
    password = StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{3,20}", message='请输入正确格式的密码！')])
    remember = StringField()

class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题')])
    content = StringField(validators=[InputRequired(message='请输入内容')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id')])


class AddCommentForm(BaseForm):
    content = StringField(validators=[InputRequired(message='请输入评论内容')])
    post_id = IntegerField(validators=[InputRequired(message='请输入帖子id')])
