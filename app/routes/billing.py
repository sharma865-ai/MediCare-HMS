from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime

from app import db
from app.models.doctor import Doctor
from app.models.billing import Billing

billing = Blueprint("billing", __name__)


# ============================
# Billing Page
# ============================
@billing.route("/admin/billing", methods=["GET", "POST"])
@login_required
def billing_page():

    doctors = Doctor.query.all()

    if request.method == "POST":

        consultation = float(request.form["consultation"] or 0)
        medicine = float(request.form["medicine"] or 0)
        lab = float(request.form["lab"] or 0)
        room = float(request.form["room"] or 0)

        discount = float(request.form.get("discount", 0) or 0)
        gst = float(request.form.get("gst", 18) or 18)

        subtotal = consultation + medicine + lab + room
        subtotal = subtotal - (subtotal * discount / 100)
        total = subtotal + (subtotal * gst / 100)

        bill_number = f"BILL-{datetime.now().strftime('%Y%m%d')}-{Billing.query.count()+1:03}"

        bill = Billing(

            bill_number=bill_number,

            patient_name=request.form["patient_name"],

            doctor_name=request.form["doctor_name"],

            consultation=consultation,

            medicine=medicine,

            lab=lab,

            room=room,

            discount=discount,

            gst=gst,

            total=total,

            payment_method=request.form["payment_method"],

            payment_status=request.form["payment_status"]

        )

        db.session.add(bill)
        db.session.commit()

        flash("Bill Generated Successfully!", "success")

        return redirect(url_for("billing.billing_list"))

    return render_template(
        "billing/index.html",
        doctors=doctors
    )


# ============================
# Billing History
# ============================
@billing.route("/admin/billing/list")
@login_required
def billing_list():

    search = request.args.get("search")

    if search:

        bills = Billing.query.filter(
            Billing.patient_name.ilike(f"%{search}%")
        ).all()

    else:

        bills = Billing.query.order_by(
            Billing.id.desc()
        ).all()

    return render_template(
        "billing/list.html",
        bills=bills,
        search=search
    )

     # ============================
# Print Bill
# ============================
@billing.route("/admin/billing/print/<int:bill_id>")
@login_required
def print_bill(bill_id):

    bill = Billing.query.get_or_404(bill_id)

    return render_template(
        "billing/print.html",
        bill=bill
    )


# ============================
# Delete Bill
# ============================
@billing.route("/admin/billing/delete/<int:bill_id>")
@login_required
def delete_bill(bill_id):

    bill = Billing.query.get_or_404(bill_id)

    db.session.delete(bill)

    db.session.commit()

    flash("Bill Deleted Successfully!", "success")

    return redirect(url_for("billing.billing_list"))