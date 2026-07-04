from flask import Blueprint, render_template, request, redirect, url_for, flash

from app import db, bcrypt
from app.models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("auth/login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        role = request.form.get("role")

        # Check existing email
        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already registered!", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            password=hashed_password,
            role=role
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful! Please Login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")