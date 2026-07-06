from app import db


class Billing(db.Model):

    __tablename__ = "billing"

    id = db.Column(db.Integer, primary_key=True)

    bill_number = db.Column(db.String(20), unique=True)

    patient_name = db.Column(db.String(100), nullable=False)

    doctor_name = db.Column(db.String(100), nullable=False)

    consultation = db.Column(db.Float, default=0)

    medicine = db.Column(db.Float, default=0)

    lab = db.Column(db.Float, default=0)

    room = db.Column(db.Float, default=0)

    discount = db.Column(db.Float, default=0)

    gst = db.Column(db.Float, default=18)

    total = db.Column(db.Float)

    payment_method = db.Column(db.String(50))

    payment_status = db.Column(db.String(20))

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )