from app import db

class Coach(db.Model):

    __tablename__="coaches"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reg_number = db.Column(db.String(11), nullable=False)
    origin = db.Column(db.String(30), nullable=False)
    destination = db.Column(db.String(30), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    drivers = db.relationship("Driver", backref="coach", lazy=True)

    def __init__(self, reg_number, origin, destination, departure_time):
        self.reg_number = reg_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time

    def add_driver(self, name):
        o = Driver(name=name, coach_id=self.id)
        db.session.add(o)
        db.session.commit()

    def __repr__(self):
        return f"{self.reg_number} from {self.origin} to {self.destination}"



class Driver(db.Model):

    __tablename__="drivers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey("coaches.id"), nullable=False)

    def __repr__(self):
        return f"{self.name}"
