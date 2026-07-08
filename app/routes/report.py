from flask import Blueprint, render_template
from flask_login import login_required

from app.models.room import Room
from app.models.bed import Bed
from app.models.operation_theatre import OperationTheatre

report = Blueprint("report", __name__)


@report.route("/admin/reports")
@login_required
def report_dashboard():

    rooms = Room.query.all()
    beds = Bed.query.all()

    room_count = Room.query.count()
    bed_count = Bed.query.count()

    icu_count = Room.query.filter_by(
        room_type="ICU"
    ).count()

    ot_count = OperationTheatre.query.count()

    return render_template(
        "report/dashboard.html",
        rooms=rooms,
        beds=beds,
        room_count=room_count,
        bed_count=bed_count,
        icu_count=icu_count,
        ot_count=ot_count
    )