from flask import Blueprint, render_template
from flask_login import login_required

patient = Blueprint("patient", __name__)

@patient.route("/patient/dashboard")
@login_required
def patient_dashboard():
    return render_template("patient/dashboard.html")