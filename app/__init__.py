from flask import Flask
from .models import db
from .views import api_blueprint


def Flask_App():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
