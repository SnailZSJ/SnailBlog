# -*- coding:gb2312 -*-
from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(Form):
    name = StringField('��������ǣ�', validators=[Required()])
    submit = SubmitField('Submit')

class EditProfileForm(Form):
    name = StringField('����', validators=[Length(0, 64)])
    location = StringField('��ס��', validators=[Length(0, 64)])
    about_me = TextAreaField('һ�仰����')
    submit = SubmitField('����')

class EditProfileAdminForm(Form):
    email = StringField('����', validators=[Required(), Length(1, 64), Email()])
    username = StringField('�ǳ�', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z0-9_.]*$', 0, '�û���������ĸ�����֡�����»���')])
    confirmed = BooleanField('�˻�ȷ��')
    role = SelectField('�û�Ȩ��', coerce=int)
    name = StringField('����', validators=[Length(0, 64)])
    location = StringField('��ס��', validators=[Length(0, 64)])
    about_me = TextAreaField('һ�仰����')
    submit = SubmitField('����')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('�����ѱ�ע��')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('�ǳ��ѱ�ʹ��')

class PostForm(Form):
    body = PageDownField("�ʾ�����˼��", validators=[Required()])
    submit = SubmitField('����')

class CommentForm(Form):
    body = StringField('���˵���䣺', validators=[Required()])
    submit = SubmitField('����')
