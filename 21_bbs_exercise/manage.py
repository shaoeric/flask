from flask_script import Manager
from bbs_exercise import create_app
from flask_migrate import MigrateCommand, Migrate
from exts import db
from apps.cms import models as cms_models
from apps.front import models as front_models

app = create_app()
CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPermission
FrontUser = front_models.FrontUser

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.option("-u", "--username", dest='username')
@manager.option("-p", "--password", dest='password')
@manager.option("-e", "--email", dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()

@manager.command
def create_role():
    #     访问者
    visitor = CMSRole(name='访问者', desc='只能访问相关数据，不能修改')
    visitor.permissions = CMSPermission.VISITOR

    # 运营
    operator = CMSRole(name='运营', desc='可以修改个人信息，管理帖子 评论 前台用户')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | \
                           CMSPermission.FRONTUSER

    # 管理员
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | \
                        CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 开发者
    developer = CMSRole(name='开发者', desc='开发人员专用')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.command
def test_permission():
    user = CMSUser.query.first()
    if user.has_permission(CMSPermission.VISITOR):
        print('这个用户有访客权限')
    else:
        print('这个用户没有访客权限')

@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('添加用户角色成功')
        else:
            print('不存在这个角色%s' % role)
    else:
        print('不存在这个用户%s' % email)

@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--passwpord', dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
