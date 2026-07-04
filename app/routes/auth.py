from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app import db, bcrypt
from app.models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            login_user(user)

            flash("Login Successful!", "success")

            # Role Based Redirect

            if user.role == "admin":
                return redirect("/admin/dashboard")

            elif user.role == "doctor":
                return redirect("/doctor/dashboard")

            elif user.role == "receptionist":
                return redirect("/receptionist/dashboard")

            else:
                return redirect("/patient/dashboard")

        flash("Invalid Email or Password!", "danger")

    return render_template("auth/login.html")


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged Out Successfully!", "success")

    return redirect(url_for("auth.login"))