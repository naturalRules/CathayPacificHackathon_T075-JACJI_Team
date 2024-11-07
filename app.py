from flask import Flask, request, redirect, render_template, url_for
from api_views import api
from db_init import initialize_db
from models import FlightWaste

def create_app():
    app = Flask(__name__)
    initialize_db()
    app.register_blueprint(api, url_prefix="/api")

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # 获取表单数据
            flight_number = request.form.get('FlightNumber')
            date_time = request.form.get('DateTime')
            waste_type = request.form.get('WasteType')
            waste_weight = request.form.get('WasteWeight', 0.0)
            waste_source = request.form.get('WasteSource')
            aircraft_type = request.form.get('AircraftType')
            disposal_method = request.form.get('DisposalMethod')
            flight_origin = request.form.get('FlightOrigin')
            flight_destination = request.form.get('FlightDestination')
            passenger_count = request.form.get('PassengerCount', 0)
            crew_count = request.form.get('CrewCount', 0)
            flight_duration = request.form.get('FlightDuration', 0.0)
            notes = request.form.get('Notes')

            # 创建数据库记录
            FlightWaste.create(
                FlightNumber=flight_number,
                DateTime=date_time,
                WasteType=waste_type,
                WasteWeight=waste_weight,
                WasteSource=waste_source,
                AircraftType=aircraft_type,
                DisposalMethod=disposal_method,
                FlightOrigin=flight_origin,
                FlightDestination=flight_destination,
                PassengerCount=passenger_count,
                CrewCount=crew_count,
                FlightDuration=flight_duration,
                Notes=notes
            )

            return redirect(url_for('index'))

        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
