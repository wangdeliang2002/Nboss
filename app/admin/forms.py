# _*_ coding: utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField,DecimalField,SelectField
from wtforms.validators import DataRequired, ValidationError,Length
from app.models import Admin


class LoginForm(FlaskForm):
    """
    管理员登录表单
    """
    manager = StringField(
        label="管理员名",
        validators=[
            DataRequired("管理员名不能为空")
        ],
        description="管理员名",
        render_kw={
            "class": "manager",
            "placeholder": "请输入管理员名！",
        }
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空")
        ],
        description="密码",
        render_kw={
            "class": "password",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "login_ok",
        }
    )

    # 验证账号，命名规则：validate_ + 字段名。如果要验证密码，则可以创建函数validate_pwd
    def validate_manager(self, field):
        account = field.data
        admin = Admin.query.filter_by(manager=account).count()
        if admin == 0:
            raise ValidationError("账号不存在! ")


class GoodsForm(FlaskForm):
    name = StringField(
        label="设备名称",
        validators=[
            DataRequired("设备名称不能为空！"),
        ],
        description="设备名称",
        render_kw={
            "class": "Style_text",
            "placeholder": "请输入设备名称！",
            "size": "50"
        }
    )
    supercat_id = SelectField(
        label="大分类",
        validators=[
            DataRequired("请选择大分类！")
        ],
        coerce=int,
        description="大分类",
        render_kw={
            "class": "form-control",
        }
    )

    subcat_id = SelectField(
        label="小分类",
        validators=[
            DataRequired("请选择小分类！")
        ],
        coerce=int,
        description="小分类",
        render_kw={
            "class": "form-control",
        }
    )
    picture = StringField(
        label="图片名称",
        validators=[
            DataRequired("图片名称不能为空！")
        ],
        description="图片名称",
        render_kw={
            "class": "Style_upload",
            "placeholder": "请输入图片名称！"
        }
    )

    introduction = TextAreaField(
        label=" 设备简介",
        validators=[
            DataRequired(" 设备简介不能为空！")
        ],
        description=" 设备简介",
        render_kw={
            "class": "textarea",
            "rows": 5
        }
    )
    right = StringField(
        label="使用权限",
        validators=[
            DataRequired("设备名称不能为空！"),
        ],
        description="设备名称",
        render_kw={
            "class": "Style_text",
            "placeholder": "请输入设备名称！",
            "size": "50"
        }
    )
    device_ip = StringField(
        label="管理地址",
        validators=[
            DataRequired("管理地址不能为空！"),
        ],
        description="管理地址",
        render_kw={
            "class": "Style_text",
            "placeholder": "请输入设备管理地址！",
            "size": "50"
        }
    )
    username = StringField(
        label="登录用户",
        validators=[
            DataRequired("登录用户不能为空！"),
        ],
        description="登录用户",
        render_kw={
            "class": "Style_text",
            "placeholder": "请输入登录用户！",
            "size": "50"
        }
    )
    password = StringField(
        label="用户密码",
        validators=[
            DataRequired("用户密码不能为空！"),
        ],
        description="用户密码",
        render_kw={
            "class": "Style_text",
            "placeholder": "请输入用户密码！",
            "size": "50"
        }
    )
    submit = SubmitField(
        '保存',
        render_kw={
            "class": "btn_bg_short",
        }
    )


