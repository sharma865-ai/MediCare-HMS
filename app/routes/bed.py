from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.bed import Bed
from app.models.room import Room

bed = Blueprint("bed", __name__)


# =========================
# Bed List
# =========================
@bed.route("/admin/beds")
@login_required
def bed_list():

    beds = Bed.query.all()

    return render_template(
        "bed/dashboard.html",
        beds=beds
    )


# =========================
# Add Bed
# =========================
@bed.route("/admin/beds/add", methods=["GET", "POST"])
@login_required
def add_bed():

    rooms = Room.query.all()

    if request.method == "POST":

        new_bed = Bed(

            bed_number=request.form["bed_number"],

            room_id=request.form["room_id"],

            status=request.form["status"]

        )

        db.session.add(new_bed)
        db.session.commit()

        return redirect(url_for("bed.bed_list"))

    return render_template(
        "bed/add.html",
        rooms=rooms
    )


# =========================
# Edit Bed
# =========================
@bed.route("/admin/beds/edit/<int:bed_id>", methods=["GET", "POST"])
@login_required
def edit_bed(bed_id):

    bed_data = Bed.query.get_or_404(bed_id)

    rooms = Room.query.all()

    if request.method == "POST":

        bed_data.bed_number = request.form["bed_number"]
        bed_data.room_id = request.form["room_id"]
        bed_data.status = request.form["status"]

        db.session.commit()

        return redirect(url_for("bed.bed_list"))

    return render_template(
        "bed/add.html",
        bed=bed_data,
        rooms=rooms
    )


# =========================
# Delete Bed
# =========================
@bed.route("/admin/beds/delete/<int:bed_id>")
@login_required
def delete_bed(bed_id):

    bed_data = Bed.query.get_or_404(bed_id)

    db.session.delete(bed_data)
    db.session.commit()

    return redirect(url_for("bed.bed_list"))