# from ..base.databasecontroller import DatabaseController
# from classes.base.persisten.databasecontroller import DatabaseController
from classes.base.databasecontroller import DatabaseController

# Erstelle eine Instanz der DatabaseController-Klasse
db_controller = DatabaseController("example.db")

# Stelle eine Verbindung zur Datenbank her
db_controller.connect()

# Führe eine Abfrage aus, um eine Tabelle zu erstellen (falls sie noch nicht existiert)
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);
"""
db_controller.execute_query(create_table_query)

# Füge Daten in die Datenbank ein
user_data = ("user1", "user1@email.com")
db_controller.insert_data("users", ["username", "email"], user_data)

# Rufe Daten aus der Datenbank ab
rows = db_controller.select_data("users")
if rows:
    for row in rows:
        print(row)

# Lösche Daten aus der Datenbank
delete_condition = "username = ?"
db_controller.delete_data("users", delete_condition, ("user1",))

# Aktualisiere Daten in der Datenbank
update_condition = "username = ?"
db_controller.update_data(
    "users",
    "email = ?",
    update_condition,
    (
        "updated@email.com",
        "user2",
    ),
)

# Trenne die Verbindung zur Datenbank
db_controller.disconnect()
