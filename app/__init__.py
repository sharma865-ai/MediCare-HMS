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

    # ==========================
    # Blueprints
    # ==========================

    from app.routes.home import home
    from app.routes.auth import auth
    from app.routes.patient import patient
    from app.routes.appointment import appointment
    from app.routes.admin import admin
    from app.routes.doctor import doctor
    from app.routes.department import department
    from app.routes.billing import billing
    from app.routes.room import room
    from app.routes.bed import bed
    from app.routes.report import report
    from app.routes.operation_theatre import operation_theatre
    from app.routes.admission import admission
    from app.routes.receptionist import receptionist

    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(patient)
    app.register_blueprint(appointment)
    app.register_blueprint(admin)
    app.register_blueprint(doctor)
    app.register_blueprint(department)
    app.register_blueprint(billing)
    app.register_blueprint(room)
    app.register_blueprint(bed)
    app.register_blueprint(report)
    app.register_blueprint(operation_theatre)
    app.register_blueprint(admission)
    app.register_blueprint(receptionist)

    # ==========================
    # Database Models
    # ==========================

    with app.app_context():

        from app.models.user import User
        from app.models.department import Department
        from app.models.doctor import Doctor
        from app.models.room import Room
        from app.models.bed import Bed
        from app.models.billing import Billing
        from app.models.admission import Admission
        from app.models.operation_theatre import OperationTheatre

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        db.create_all()

    return app