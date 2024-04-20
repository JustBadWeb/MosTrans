from data.db_session import sessions

from backend.application import application
from flask import render_template, request, jsonify


@application.route("/", methods=["GET"])
def index():
    """Website home page"""

    from data.models import Line, Station, PassengerFlow

    date = request.args.get('date')
    station_name = request.args.get('station_name')

    station = sessions["train_database"].query(Station).filter_by(name=station_name).first()
    if station is not None:
        answer = sessions["train_database"].query(PassengerFlow).filter_by(station_id=station.id, ymd=date).first()
        if answer is not None:
            answer = answer.count
    else:
        answer = None

    data = dict()
    data["lines"] = dict()
    for line in sessions["train_database"].query(Line).order_by(Line.name).all():
        data["lines"][line.name] = [station.name for station in sessions["train_database"].query(Station).filter_by(line_id=line.id).order_by(Station.name).all()]
    data["stations"] = [station.name for station in sessions["train_database"].query(Station).order_by(Station.name).all()]

    # return jsonify(**data, answer=answer)
    return render_template("index.html", data=data, answer=answer)
