from flask import Blueprint, url_for

user_bp = Blueprint('user', __name__, url_prefix='/user')
                                        #  对url添加前缀

# 个人中心url 视图函数
@user_bp.route('/profile/')
def profile():
    # 一个蓝图中进行反转url也要加上蓝图的名字
    print(url_for('user.settings'))
    return '个人中心页面'

@user_bp.route('/settings/')
def settings():
    return '个人中心设置页面'