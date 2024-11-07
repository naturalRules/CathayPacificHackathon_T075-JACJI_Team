from models import db, FlightWaste

def initialize_db():
    with db:
        db.create_tables([FlightWaste])

