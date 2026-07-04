from app import db


class Doctor(db.Model):

    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    specialization = db.Column(db.String(100))

    experience = db.Column(db.Integer)

    phone = db.Column(db.String(15))

    email = db.Column(db.String(120))