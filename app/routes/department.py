from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app import db
from app.models.department import Department
from app.models.doctor import Doctor

department = Blueprint("department", __name__)


# ==========================================
# Department Dashboard
# ==========================================
@department.route("/admin/departments")
@login_required
def department_dashboard():

    departments = Department.query.order_by(
        Department.id.desc()
    ).all()

    total_departments = Department.query.count()

    active_departments = Department.query.filter_by(
        status="Active"
    ).count()

    inactive_departments = Department.query.filter_by(
        status="Inactive"
    ).count()

    return render_template(
        "department/dashboard.html",
        departments=departments,
        total_departments=total_departments,
        active_departments=active_departments,
        inactive_departments=inactive_departments
    )


# ==========================================
# Add Department
# ==========================================
@department.route("/admin/departments/add", methods=["GET", "POST"])
@login_required
def add_department():

    doctors = Doctor.query.order_by(
        Doctor.full_name.asc()
    ).all()

    if request.method == "POST":

        name = request.form.get("name")
        department_code = request.form.get("department_code")
        head_doctor = request.form.get("head_doctor")
        description = request.form.get("description")
        status = request.form.get("status")

        # Duplicate Department Name

        if Department.query.filter_by(name=name).first():

            flash("Department already exists!", "danger")

            return redirect(
                url_for("department.add_department")
            )

        # Duplicate Department Code

        if Department.query.filter_by(
            department_code=department_code
        ).first():

            flash("Department Code already exists!", "danger")

            return redirect(
                url_for("department.add_department")
            )

        department = Department(

            name=name,

            department_code=department_code,

            head_doctor=head_doctor,

            description=description,

            status=status

        )

        db.session.add(department)

        db.session.commit()

        flash(
            "Department Added Successfully!",
            "success"
        )

        return redirect(
            url_for("department.department_dashboard")
        )

    return render_template(
        "department/add.html",
        doctors=doctors
    )


# ==========================================
# Edit Department
# ==========================================
@department.route(
    "/admin/departments/edit/<int:department_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_department(department_id):

    department = Department.query.get_or_404(
        department_id
    )

    doctors = Doctor.query.order_by(
        Doctor.full_name.asc()
    ).all()

    if request.method == "POST":

        name = request.form.get("name")
        department_code = request.form.get("department_code")

        # Duplicate Name

        existing_name = Department.query.filter(
            Department.name == name,
            Department.id != department_id
        ).first()

        if existing_name:

            flash(
                "Department already exists!",
                "danger"
            )

            return redirect(
                url_for(
                    "department.edit_department",
                    department_id=department_id
                )
            )

        # Duplicate Code

        existing_code = Department.query.filter(
            Department.department_code == department_code,
            Department.id != department_id
        ).first()

        if existing_code:

            flash(
                "Department Code already exists!",
                "danger"
            )

            return redirect(
                url_for(
                    "department.edit_department",
                    department_id=department_id
                )
            )

        department.name = name
        department.department_code = department_code
        department.head_doctor = request.form.get(
            "head_doctor"
        )
        department.description = request.form.get(
            "description"
        )
        department.status = request.form.get(
            "status"
        )

        db.session.commit()

        flash(
            "Department Updated Successfully!",
            "success"
        )

        return redirect(
            url_for("department.department_dashboard")
        )

    return render_template(
        "department/add.html",
        department=department,
        doctors=doctors
    )


# ==========================================
# Delete Department
# ==========================================
@department.route(
    "/admin/departments/delete/<int:department_id>"
)
@login_required
def delete_department(department_id):

    department = Department.query.get_or_404(
        department_id
    )

    db.session.delete(department)

    db.session.commit()

    flash(
        "Department Deleted Successfully!",
        "success"
    )

    return redirect(
        url_for("department.department_dashboard")
    )