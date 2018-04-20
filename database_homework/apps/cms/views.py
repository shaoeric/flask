from flask import Blueprint, render_template, redirect

bp = Blueprint('cms', __name__, url_prefix='/cms')

@bp.route('/')
def index():
    return render_template('cms/index.html')


@bp.route('/tab_panel/')
def tab_panel():
    return render_template('cms/tab-panel.html')

@bp.route('/table/')
def table():
    return render_template('cms/table.html')

