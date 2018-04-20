from .views import bp
from flask import session, g
import config
from .models import CMSUser, CMSPermission

# init.py中执行hooks， 使得关联整个项目
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user

@bp.context_processor
def cms_context_processor():
    return {'CMSPermission': CMSPermission}
