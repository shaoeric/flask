from flask import Flask, Blueprint
from apps.cms import bp as cms_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(cms_bp)
    return app

app = create_app()
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
