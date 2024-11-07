from peewee import Model, SqliteDatabase, IntegerField, TextField

# 数据库实例
db = SqliteDatabase('database/waste.db')

class FlightWaste(Model):
    FlightNumber = TextField()
    DateTime = TextField()
    WasteType = TextField()
    WasteWeight = TextField()
    WasteSource = TextField()
    AircraftType = TextField()
    DisposalMethod = TextField()
    FlightOrigin = TextField()
    FlightDestination = TextField()
    PassengerCount = IntegerField()
    CrewCount = IntegerField()
    FlightDuration = TextField()
    Notes = TextField(null=True)

    class Meta:
        database = db
