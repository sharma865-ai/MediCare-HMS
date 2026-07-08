from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from flask_login import current_user
from app.models.user import User
from app.models.appointment import Appointment

from app import db
from app.models.doctor import Doctor
from sqlalchemy import or_

doctor = Blueprint("doctor", __name__)

# =========================
# Doctor Dashboard
# =========================
@doctor.route("/doctor/dashboard")
@login_required
def doctor_dashboard():

    patient_count = User.query.filter_by(role="patient").count()

    appointment_count = Appointment.query.count()

    prescription_count = 0

    emergency_count = 0

    appointments = Appointment.query.order_by(
        Appointment.appointment_date.desc()
    ).limit(10).all()
 
    return render_template(
    "doctor/doctor_dashboard.html",
        patient_count=patient_count,
        appointment_count=appointment_count,
        prescription_count=prescription_count,
        emergency_count=emergency_count,
        appointments=appointments,
        current_user=current_user
    )

# =========================
# Doctor List
# =========================
@doctor.route("/admin/doctors")
@login_required
def doctor_list():

    search = request.args.get("search")

    if search:

        doctors = Doctor.query.filter(

            or_(

                Doctor.full_name.ilike(f"%{search}%"),
                Doctor.specialization.ilike(f"%{search}%"),
                Doctor.email.ilike(f"%{search}%")

            )

        ).all()

    else:

        doctors = Doctor.query.all()

    return render_template(
        "doctor/dashboard.html",
        doctors=doctors,
        search=search
    )


# =========================
# Add Doctor
# =========================
@doctor.route("/admin/doctors/add", methods=["GET", "POST"])
@login_required
def add_doctor():

    if request.method == "POST":

        new_doctor = Doctor(

            full_name=request.form["full_name"],
            specialization=request.form["specialization"],
            email=request.form["email"],
            phone=request.form["phone"],
            qualification=request.form["qualification"],
            experience=request.form["experience"],
            consultation_fee=request.form["consultation_fee"]

        )

        db.session.add(new_doctor)
        db.session.commit()

        return redirect(url_for("doctor.doctor_list"))

    return render_template("doctor/add.html")

# ===========================
# Delete Doctor
# ===========================

@doctor.route("/admin/doctors/delete/<int:doctor_id>")
@login_required
def delete_doctor(doctor_id):

    doctor = Doctor.query.get_or_404(doctor_id)

    db.session.delete(doctor)

    db.session.commit()

    return redirect(url_for("doctor.doctor_list"))


# ===========================
# Edit Doctor
# ===========================

@doctor.route("/admin/doctors/edit/<int:doctor_id>", methods=["GET","POST"])
@login_required
def edit_doctor(doctor_id):

    doctor = Doctor.query.get_or_404(doctor_id)

    if request.method == "POST":

        doctor.full_name = request.form["full_name"]
        doctor.specialization = request.form["specialization"]
        doctor.email = request.form["email"]
        doctor.phone = request.form["phone"]
        doctor.qualification = request.form["qualification"]
        doctor.experience = request.form["experience"]
        doctor.consultation_fee = request.form["consultation_fee"]

        db.session.commit()

        return redirect(url_for("doctor.doctor_list"))

    return render_template("doctor/add.html", doctor=doctor)