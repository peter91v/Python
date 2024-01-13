# from test.testpersistent import test_auto_persistence
import classes.persistent.sensor as Sensor
import test
import classes.base.databasecontroller as DBController
import datetime as dt

print("hallo")
# test_auto_persistence()
host = "localhost"
user = "root"
password = "varP91!!"
database = "temperature"

controller_mysql = DBController.DatabaseController(host, user, password, database)
# controller_mysql.connect()
# where_statment = "date > current_date -1000"
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
    db_connection=controller_mysql,
)
sen.save()

sen.delete()

# sensors_table = Sensor.Sensors(db_connection=controller_mysql)

print(sen.ShortName)
# sen.DB_Connection = controller_mysql
sen2 = Sensor.Sensors(db_connection=controller_mysql)
# sen2.db_connection = controller_mysql.connection
sen2 = sen2.load(110)
print(f"StandortId: {sen2.StandortId}")
print(f"Text: {sen2.Text}")
print(f"ShortName: {sen2.ShortName}")
print(f"SensorId: {sen2.SensorId}")

sen2.Text = 'Heizraum Kaltwasser test'
sen2.save()
# (601,"Test","Test","102563", "2023-12-08", "17:34:11",19.45)

# Sensor.Sensor.save_instance(x)

# x.save

# y = Sensor.Sensor.load_data()
# print(y)
controller_mysql.disconnect()
