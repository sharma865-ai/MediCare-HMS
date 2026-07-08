from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from datetime import datetime

from app import db
from app.models.admission import Admission
from app.models.user import User
from app.models.doctor import Doctor
from app.models.room import Room
from app.models.bed import Bed

admission = Blueprint("admission", __name__)


# =========================
# Admission List
# =========================
@admission.route("/admin/admissions")
@login_required
def admission_list():

    admissions = Admission.query.all()

    return render_template(
        "admission/dashboard.html",
        admissions=admissions
    )


# =========================
# Add Admission
# =========================
@admission.route("/admin/admissions/add", methods=["GET", "POST"])
@login_required
def add_admission():

    patients = User.query.filter_by(role="patient").all()
    doctors = Doctor.query.all()
    rooms = Room.query.filter_by(status="Available").all()
    beds = Bed.query.filter_by(status="Available").all()

    if request.method == "POST":

        admission = Admission(

            patient_id=request.form["patient_id"],
            doctor_id=request.form["doctor_id"],
            room_id=request.form["room_id"],
            bed_id=request.form["bed_id"],

            admission_date=datetime.strptime(
                request.form["admission_date"],
                "%Y-%m-%d"
            ).date(),

            status="Admitted"

        )

        db.session.add(admission)

        room = Room.query.get(request.form["room_id"])
        bed = Bed.query.get(request.form["bed_id"])

        room.status = "Occupied"
        bed.status = "Occupied"

        db.session.commit()

        return redirect(
            url_for("admission.admission_list")
        )

    return render_template(
        "admission/add.html",
        patients=patients,
        doctors=doctors,
        rooms=rooms,
        beds=beds
    )