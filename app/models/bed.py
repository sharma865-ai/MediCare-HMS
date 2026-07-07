from app import db


class Bed(db.Model):

    __tablename__ = "beds"

    id = db.Column(db.Integer, primary_key=True)

    bed_number = db.Column(db.String(20), unique=True, nullable=False)

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Available"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    room = db.relationship("Room", backref="beds")