from flask import Blueprint, request, jsonify
from models import FlightWaste

api = Blueprint('api', __name__)

@api.route('/add_waste', methods=['POST'])
def add_waste():
    data = request.get_json()
    try:
        flight_waste = FlightWaste.create(
            FlightNumber=data['FlightNumber'],
            DateTime=data['DateTime'],
            WasteType=data['WasteType'],
            WasteWeight=data['WasteWeight'],
            WasteSource=data['WasteSource'],
            AircraftType=data['AircraftType'],
            DisposalMethod=data['DisposalMethod'],
            FlightOrigin=data['FlightOrigin'],
            FlightDestination=data['FlightDestination'],
            PassengerCount=data['PassengerCount'],
            CrewCount=data['CrewCount'],
            FlightDuration=data['FlightDuration'],
            Notes=data.get('Notes')  # Notes字段是可选的
        )
        response = {
            'status': 'success',
            'data': {'id': flight_waste.id}
        }
        return jsonify(response), 201
    except KeyError as e:
        return jsonify({'status': 'error', 'message': f'Missing field {str(e)}'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

