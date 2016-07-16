# -*- coding:gb2312 -*-
from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(Form):
    name = StringField('你的姓名是？', validators=[Required()])
    submit = SubmitField('Submit')

class EditProfileForm(Form):
    name = StringField('姓名', validators=[Length(0, 64)])
    location = StringField('居住地', validators=[Length(0, 64)])
    about_me = TextAreaField('一句话介绍')
    submit = SubmitField('保存')

class EditProfileAdminForm(Form):
    email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
    username = StringField('昵称', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z0-9_.]*$', 0, '用户名仅限字母、数字、点或下划线')])
    confirmed = BooleanField('账户确认')
    role = SelectField('用户权限', coerce=int)
    name = StringField('姓名', validators=[Length(0, 64)])
    location = StringField('居住地', validators=[Length(0, 64)])
    about_me = TextAreaField('一句话介绍')
    submit = SubmitField('保存')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已被使用')

class PostForm(Form):
    body = PageDownField("问君何所思？", validators=[Required()])
    submit = SubmitField('发布')

class CommentForm(Form):
    body = StringField('随便说两句：', validators=[Required()])
    submit = SubmitField('发布')
