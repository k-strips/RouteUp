from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.routeup.views import routeup
from app.api.views import api

app.register_blueprint(routeup)
app.register_blueprint(api)


db.create_all()
