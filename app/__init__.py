from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    # Blueprints
    from app.routes.home import home
    from app.routes.auth import auth

    app.register_blueprint(home)
    app.register_blueprint(auth)

    with app.app_context():
        from app.models.user import User

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        db.create_all()

    return app