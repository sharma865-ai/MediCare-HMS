from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

from app import db
from app.models.doctor import Doctor
from app.models.department import Department
from app.models.user import User
from app.models.appointment import Appointment

admin = Blueprint("admin", __name__)


# =========================
# Dashboard
# =========================
@admin.route("/admin/dashboard")
@login_required
def admin_dashboard():

    doctor_count = Doctor.query.count()
    patient_count = User.query.filter_by(role="patient").count()
    appointment_count = Appointment.query.count()
    department_count = Department.query.count()

    return render_template(
        "admin/dashboard.html",
        doctor_count=doctor_count,
        patient_count=patient_count,
        appointment_count=appointment_count,
        department_count=department_count
    )


# =========================
# Appointment List
# =========================
@admin.route("/admin/appointments")
@login_required
def appointment_list():

    appointments = Appointment.query.all()

    return render_template(
        "admin/appointments.html",
        appointments=appointments
    )


# =========================
# Approve Appointment
# =========================
@admin.route("/admin/appointments/approve/<int:appointment_id>")
@login_required
def approve_appointment(appointment_id):

    appointment = Appointment.query.get_or_404(appointment_id)

    appointment.status = "Approved"

    db.session.commit()

    return redirect(url_for("admin.appointment_list"))


# =========================
# Reject Appointment
# =========================
@admin.route("/admin/appointments/reject/<int:appointment_id>")
@login_required
def reject_appointment(appointment_id):

    appointment = Appointment.query.get_or_404(appointment_id)

    appointment.status = "Rejected"

    db.session.commit()

    return redirect(url_for("admin.appointment_list"))


# =========================
# Delete Appointment
# =========================
@admin.route("/admin/appointments/delete/<int:appointment_id>")
@login_required
def delete_appointment(appointment_id):

    appointment = Appointment.query.get_or_404(appointment_id)

    db.session.delete(appointment)

    db.session.commit()

    return redirect(url_for("admin.appointment_list"))

    # ===========================
# Patient List
# ===========================

@admin.route("/admin/patients")
@login_required
def patient_list():

    patients = User.query.filter_by(role="patient").all()

    return render_template(
        "admin/patients.html",
        patients=patients
    )


# ===========================
# Delete Patient
# ===========================

@admin.route("/admin/patients/delete/<int:patient_id>")
@login_required
def delete_patient(patient_id):

    patient = User.query.get_or_404(patient_id)

    db.session.delete(patient)

    db.session.commit()

    return redirect(url_for("admin.patient_list"))