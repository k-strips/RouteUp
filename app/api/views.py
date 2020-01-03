from flask import Blueprint, request, jsonify, \
                  url_for, g

from app.routeup.model import Coach, Driver

api = Blueprint("api", __name__, url_prefix="/api/v1")

@api.route("/coach/<int:coach_id>")
def view_coach_api(coach_id):
    #return details of a single coach

    #search for coach
    coach = Coach.query.get(coach_id)
    if coach is None:
        return jsonify({"empty": "No Such Coach"}), 422

    drivers = coach.drivers
    driver_names = []
    for driver in drivers:
        driver_names.append(driver.name)
    return jsonify({
        "reg_number": coach.reg_number,
        "origin": coach.origin,
        "destination": coach.destination,
        "departure_time": coach.departure_time,
        "drivers": driver_names
    })


@api.route("/coaches")
def view_coaches_api():
    coaches = Coach.query.all()
    list = []
    for coach in coaches:
        coach = {
          "reg_number": coach.reg_number,
          "origin": coach.origin,
          "destination": coach.destination,
          "departure_time": coach.departure_time
        }
        list.append(coach)
    return jsonify({
    "coaches": list
    })
