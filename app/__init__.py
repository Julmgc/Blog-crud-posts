from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.views import posts_view
    posts_view.init_app(app)

    return app
