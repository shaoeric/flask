from functools import wraps
from flask import session, redirect, url_for

def login_reqired(func):
    # 判断是否登录/服务器重启，将user_id解析出来就说明是登录状态
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        if user_id:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
