# from test.testpersistent import test_auto_persistence
import classes.persistent.sensor as Sensor
import test
import classes.base.databasecontroller as DBController
import datetime as dt

print("hallo")

host = "localhost"
user = "root"
password = "varP91!!"
database = "temperature"

controller_mysql = DBController.DatabaseController(host, user, password, database)
controller_mysql.connect()

x = controller_mysql.select_data("sensors", "Text")

Sensor.Sensors.connection = controller_mysql.connection
print(x[1])

sen = Sensor.Sensors(
    StandortId=2,
    Text="Sensor 1",
    ShortName="S1",
    SensorId="ABC123",
    Date=dt.date(2021, 1, 1),
    time=dt.time(12, 0, 0),
    Temperature=20.0,
)

sen.save()

sen.delete()

print(sen.ShortName)
sen2 = Sensor.Sensors()
sen2 = sen2.load(110)
print(f"StandortId: {sen2.StandortId}")
print(f"Text: {sen2.Text}")
print(f"ShortName: {sen2.ShortName}")
print(f"SensorId: {sen2.SensorId}")
print(f"Temperature: {sen2.TEMPERATURE}")

sen2.Text = "Heizraum Kaltwasser"
sen2.save()

controller_mysql.disconnect()
