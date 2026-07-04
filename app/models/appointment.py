from app import db


class Appointment(db.Model):

    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    patient_name = db.Column(db.String(100))

    doctor_name = db.Column(db.String(100))

    appointment_date = db.Column(db.Date)

    appointment_time = db.Column(db.Time)

    status = db.Column(db.String(30), default="Pending")