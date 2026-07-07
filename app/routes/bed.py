from flask import Blueprint, render_template
from flask_login import login_required

from app.models.bed import Bed

bed = Blueprint("bed", __name__)


@bed.route("/admin/beds")
@login_required
def bed_list():

    beds = Bed.query.all()

    return render_template(
        "bed/dashboard.html",
        beds=beds
    )