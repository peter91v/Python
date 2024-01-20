import base.databasecontroller as DBController
from autopersistentgenerator import AutoPersistentGenerator

host = "localhost"
user = "root"
password = "varP91!!"
database = "temperature"

controller_mysql = DBController.DatabaseController(host, user, password, database)
controller_mysql.connect()

columns = []
columns = controller_mysql.get_columns("weather_forecast", data_type=True)
print(columns[0]['COLUMN_NAME'])

generator = AutoPersistentGenerator(
    "D:\DEV\PythonProject\classes\persistent", "s102"
)
generator.CreateFile(columns)
