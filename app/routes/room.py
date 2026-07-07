from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.room import Room

room = Blueprint("room", __name__)


@room.route("/admin/rooms")
@login_required
def room_list():

    rooms = Room.query.all()

    return render_template(
        "room/dashboard.html",
        rooms=rooms
    )


@room.route("/admin/rooms/add", methods=["GET", "POST"])
@login_required
def add_room():

    if request.method == "POST":

        new_room = Room(

            room_number=request.form["room_number"],

            room_type=request.form["room_type"],

            floor=request.form["floor"],

            charges=request.form["charges"],

            status=request.form["status"]

        )

        db.session.add(new_room)
        db.session.commit()

        return redirect(url_for("room.room_list"))

    return render_template("room/add.html")


@room.route("/admin/rooms/edit/<int:room_id>", methods=["GET","POST"])
@login_required
def edit_room(room_id):

    room_data = Room.query.get_or_404(room_id)

    if request.method == "POST":

        room_data.room_number = request.form["room_number"]
        room_data.room_type = request.form["room_type"]
        room_data.floor = request.form["floor"]
        room_data.charges = request.form["charges"]
        room_data.status = request.form["status"]

        db.session.commit()

        return redirect(url_for("room.room_list"))

    return render_template(
        "room/add.html",
        room=room_data
    )


@room.route("/admin/rooms/delete/<int:room_id>")
@login_required
def delete_room(room_id):

    room_data = Room.query.get_or_404(room_id)

    db.session.delete(room_data)
    db.session.commit()

    return redirect(url_for("room.room_list"))