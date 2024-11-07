import unittest
from peewee import SqliteDatabase
from models import FlightWaste  # 假设 FlightWaste 类定义在 models 模块中

# 使用内存数据库
test_db = SqliteDatabase('database/waste.db')

class TestFlightWasteModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 将模型绑定到测试数据库并创建表
        cls.database = test_db
        cls.database.bind([FlightWaste], bind_refs=False, bind_backrefs=False)
        cls.database.connect()
        cls.database.create_tables([FlightWaste])

    @classmethod
    def tearDownClass(cls):
        # 断开和清空测试数据库
        # cls.database.drop_tables([FlightWaste])
        cls.database.close()

    def test_create_flight_waste_record(self):
        # Define the test records data
        data = {
            'FlightNumber': 'AA123',
            'DateTime': '2023-10-15 13:45:00',
            'WasteType': 'Plastic',
            'WasteWeight': '50.5',
            'WasteSource': 'Onboard Service',
            'AircraftType': 'A320',
            'DisposalMethod': 'Recycling',
            'FlightOrigin': 'JFK',
            'FlightDestination': 'LAX',
            'PassengerCount': 180,
            'CrewCount': 8,
            'FlightDuration': '6.5',
            'Notes': 'Test flight waste entry'
        }

        # Create a new record
        flight_waste = FlightWaste.create(**data)

        # Validate that the record is stored as expected
        self.assertIsNotNone(flight_waste.id)  # check if ID (primary key) is assigned
        self.assertEqual(flight_waste.FlightNumber, 'AA123')
        self.assertEqual(flight_waste.WasteType, 'Plastic')
        self.assertEqual(flight_waste.WasteWeight, '50.5')  # Text for weight here for your test example
        self.assertEqual(flight_waste.DisposalMethod, 'Recycling')

        # Further tests can assert successful query, retrieval or any other validation as required

if __name__ == '__main__':
    unittest.main()
