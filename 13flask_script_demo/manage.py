from flask_script import Manager
from flask_script_demo import app, BackendUser, db

manager = Manager(app)

# cmd中切换到当前虚拟环境， python manage.py greet输出“你好”
@manager.command
def greet():
    print("你好")

# 传参形式
# -u是简写 --username全称  dest指定参数传递给哪个形参
# python manage,py -u eric -a 18
# @manager.option("-u", "--username", dest='username')
# @manager.option("-a", "--age", dest="age")
# def add_user(username, age):
#     print("您输入的用户名是%s, 年龄是%s" % (username, age))


# 在后台添加超级管理员的时候 不能通过url访问添加 这样不安全 所以需要用cmd这种方式添加
@manager.option("-u", "--username", dest="username")
@manager.option("-e", "--email", dest="email")
def add_user(username, email):
    user = BackendUser(username=username, email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()