from app import db


class OperationTheatre(db.Model):

    __tablename__ = "operation_theatres"

    id = db.Column(db.Integer, primary_key=True)

    ot_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    theatre_name = db.Column(
        db.String(100),
        nullable=False
    )

    doctor_name = db.Column(
        db.String(100)
    )

    status = db.Column(
        db.String(20),
        default="Available"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )