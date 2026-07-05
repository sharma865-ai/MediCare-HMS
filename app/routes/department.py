from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.department import Department

department = Blueprint("department", __name__)


@department.route("/admin/departments")
@login_required
def department_list():

    departments = Department.query.all()

    return render_template(
        "department/dashboard.html",
        departments=departments
    )


@department.route("/admin/departments/add", methods=["GET", "POST"])
@login_required
def add_department():

    if request.method == "POST":

        new_department = Department(

            name=request.form["name"],
            description=request.form["description"]

        )

        db.session.add(new_department)
        db.session.commit()

        return redirect(url_for("department.department_list"))

    return render_template("department/add.html")

# ===========================
# Delete Department
# ===========================

@department.route("/admin/departments/delete/<int:department_id>")
@login_required
def delete_department(department_id):

    department_data = Department.query.get_or_404(department_id)

    db.session.delete(department_data)

    db.session.commit()

    return redirect(url_for("department.department_list"))


# ===========================
# Edit Department
# ===========================

@department.route("/admin/departments/edit/<int:department_id>", methods=["GET", "POST"])
@login_required
def edit_department(department_id):

    department_data = Department.query.get_or_404(department_id)

    if request.method == "POST":

        department_data.name = request.form["name"]
        department_data.description = request.form["description"]

        db.session.commit()

        return redirect(url_for("department.department_list"))

    return render_template(
        "department/add.html",
        department=department_data
    )