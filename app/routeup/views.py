#Importing flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, redirect, url_for, g

from app import db

from app.routeup.form import Register_Coach, Add_Driver

from app.routeup.model import Coach, Driver

routeup = Blueprint("routeup", __name__,)

@routeup.route("/")
def index():
    coaches = Coach.query.all()
    return render_template("index.html", coaches=coaches)

@routeup.route("/coaches/<int:coach_id>")
def coach(coach_id):
    """List details about a single flight"""

    #make sure coach exists
    coach = Coach.query.get(coach_id)
    if coach is None:
        flash("No such Coach exists", "error")

    drivers = coach.drivers
    return render_template("coach.html", coach=coach, drivers=drivers)

@routeup.route("/add", methods=['GET', 'POST'])
def add():

    form = Register_Coach()
    if form.validate_on_submit():
        coach = Coach(form.reg_number.data, form.origin.data, form.destination.data, form.departure_time.data)
        db.session.add(coach)
        db.session.commit()
        flash('Coach added successfully', 'success')
        return redirect(url_for('routeup.index'))
    return render_template("update_system.html", form=form)


@routeup.route("/remove_coach/<int:id>", methods=['GET', 'POST'])
def remove(id):
    coach = Coach.query.get(id)
    db.session.delete(coach)
    db.session.commit()
    flash('No such bus Exist', 'error')
    return redirect(url_for('routeup.index'))
