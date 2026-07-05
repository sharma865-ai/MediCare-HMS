from app import db

class Doctor(db.Model):

    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    specialization = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True)

    phone = db.Column(db.String(15))

    qualification = db.Column(db.String(100))

    experience = db.Column(db.Integer)

    consultation_fee = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Doctor {self.full_name}>"