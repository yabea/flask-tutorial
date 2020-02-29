# coding:utf-8
"""
desc: 权限校验
"""
from functools import wraps
from flask import session, abort
from app.models import db, Users, Role

Permission_code = [0X01, 0X02]


def permission_can(current_user, permission):
    """
    检测用户是否有特定权限
    :param current_user
    :param permission
    :return:
    """
    print("@#" * 10)
    role_id = current_user.role_id
    print("#" * 120)
    print(role_id)
    role = db.session.query(Role).filter_by(id=role_id).first()
    return (role.permissions & permission) == permission


def permission_required(permission):
    """
    权限认证装饰器
    :param permission:
    :return:
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                flag = False
                current_user = Users.query.filter_by(id=session.get('user_id')).first()
                if current_user:
                    role_id = current_user.role_id
                    role = db.session.query(Role).filter_by(id=role_id).first()
                    if role.permissions & permission == permission:
                        flag = True
                if flag:
                    return f(*args, **kwargs)
                else:
                    abort(403)
            except:
                abort(403)
        return decorated_function
    return decorator
