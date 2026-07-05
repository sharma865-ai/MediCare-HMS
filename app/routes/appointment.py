from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime

from app import db
from app.models.appointment import Appointment
from app.models.doctor import Doctor

appointment = Blueprint("appointment", __name__)


# ==========================
# Book Appointment
# ==========================
@appointment.route("/patient/book-appointment", methods=["GET", "POST"])
@login_required
def book_appointment():

    doctors = Doctor.query.all()

    if request.method == "POST":

        appointment_date = datetime.strptime(
            request.form["appointment_date"],
            "%Y-%m-%d"
        ).date()

        appointment_time = datetime.strptime(
            request.form["appointment_time"],
            "%H:%M"
        ).time()

        new_appointment = Appointment(
            patient_id=current_user.id,
            doctor_id=int(request.form["doctor_id"]),
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=request.form["reason"]
        )

        db.session.add(new_appointment)
        db.session.commit()

        return redirect(url_for("appointment.my_appointments"))

    return render_template(
        "appointment/book.html",
        doctors=doctors
    )


# ==========================
# My Appointments
# ==========================
@appointment.route("/patient/my-appointments")
@login_required
def my_appointments():

    appointments = Appointment.query.filter_by(
        patient_id=current_user.id
    ).all()

    return render_template(
        "appointment/my_appointments.html",
        appointments=appointments
    )