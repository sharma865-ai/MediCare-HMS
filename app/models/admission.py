from app import db


class Admission(db.Model):

    __tablename__ = "admissions"

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    bed_id = db.Column(
        db.Integer,
        db.ForeignKey("beds.id"),
        nullable=False
    )

    admission_date = db.Column(db.Date)

    discharge_date = db.Column(db.Date)

    status = db.Column(
        db.String(20),
        default="Admitted"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    patient = db.relationship("User")

    doctor = db.relationship("Doctor")

    room = db.relationship("Room")

    bed = db.relationship("Bed")