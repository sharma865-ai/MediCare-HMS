from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.operation_theatre import OperationTheatre

operation_theatre = Blueprint(
    "operation_theatre",
    __name__
)


@operation_theatre.route("/admin/operation-theatres")
@login_required
def theatre_list():

    theatres = OperationTheatre.query.all()

    return render_template(
        "operation_theatre/dashboard.html",
        theatres=theatres
    )


@operation_theatre.route(
    "/admin/operation-theatres/add",
    methods=["GET", "POST"]
)
@login_required
def add_theatre():

    if request.method == "POST":

        theatre = OperationTheatre(

            ot_number=request.form["ot_number"],

            theatre_name=request.form["theatre_name"],

            doctor_name=request.form["doctor_name"],

            status=request.form["status"]

        )

        db.session.add(theatre)
        db.session.commit()

        return redirect(
            url_for("operation_theatre.theatre_list")
        )

    return render_template(
        "operation_theatre/add.html"
    )