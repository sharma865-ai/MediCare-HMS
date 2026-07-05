from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.doctor import Doctor

doctor = Blueprint("doctor", __name__)


# =========================
# Doctor List
# =========================
@doctor.route("/admin/doctors")
@login_required
def doctor_list():

    doctors = Doctor.query.all()

    return render_template(
        "doctor/dashboard.html",
        doctors=doctors
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