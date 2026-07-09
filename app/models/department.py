from datetime import datetime
from app import db


class Department(db.Model):

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False, unique=True)

    department_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    head_doctor = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Department {self.name}>"