# -*- coding:gb2312 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('����',validators=[Required(), Length(1,64),Email()])
    password = PasswordField('����', validators=[Required()])
    remember_me = BooleanField('��ס��')
    submit = SubmitField('��½')


class RegistrationForm(Form):
    email = StringField('����', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('�ǳ�', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          '�û������������ĸ�����֡�����»���')])
    password = PasswordField('����', validators=[
        Required(), EqualTo('password2', message='�������ƥ�䡣')])
    password2 = PasswordField('ȷ������', validators=[Required()])
    submit = SubmitField('ע��')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('�������˺��ѱ�ע��')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('�ǳ��ѱ�ʹ�á�')

class ChangePasswordForm(Form):
    old_password = PasswordField('������', validators=[Required()])
    password = PasswordField('������', validators=[
        Required(), EqualTo('password2', message='�������ƥ�䡣')])
    password2 = PasswordField('ȷ��������', validators=[Required()])
    submit = SubmitField('�޸�����')


class PasswordResetRequestForm(Form):
    email = StringField('����', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('��������')


class PasswordResetForm(Form):
    email = StringField('����', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('������', validators=[
        Required(), EqualTo('password2', message='�������ƥ�䡣')])
    password2 = PasswordField('ȷ������', validators=[Required()])
    submit = SubmitField('��������')

class ChangeEmailForm(Form):
    email = StringField('������', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('����', validators=[Required()])
    submit = SubmitField('��������')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')
