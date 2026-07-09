from flask import Blueprint, render_template
from flask_login import login_required
from datetime import date

from app.models.user import User
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.models.billing import Billing

receptionist = Blueprint("receptionist", __name__)


@receptionist.route("/receptionist/dashboard")
@login_required
def receptionist_dashboard():

    patient_count = User.query.filter_by(role="patient").count()

    doctor_count = Doctor.query.count()

    appointment_count = Appointment.query.filter_by(
        appointment_date=date.today()
    ).count()

    bills = Billing.query.all()

    billing_total = sum(b.total for b in bills)

    appointments = Appointment.query.order_by(
        Appointment.appointment_date.desc()
    ).limit(10).all()

    return render_template(
        "receptionist/dashboard.html",
        patient_count=patient_count,
        doctor_count=doctor_count,
        appointment_count=appointment_count,
        billing_total=billing_total,
        appointments=appointments
    )