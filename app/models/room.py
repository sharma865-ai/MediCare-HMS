from app import db


class Room(db.Model):

    __tablename__ = "rooms"

    id = db.Column(db.Integer, primary_key=True)

    room_number = db.Column(db.String(20), unique=True, nullable=False)

    room_type = db.Column(db.String(50), nullable=False)

    floor = db.Column(db.String(20))

    charges = db.Column(db.Float, nullable=False)

    status = db.Column(
        db.String(20),
        default="Available"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )