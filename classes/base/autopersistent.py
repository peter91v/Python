import mysql.connector
import pickle
from base.databasecontroller import DatabaseController
from abc import ABC, abstractmethod
import inspect


class AutoPersistentController(DatabaseController):
    def __init__(self):
        if not self.connection.is_connected:
            self.connect()

    def create_table(self):
        cursor = self.connection.cursor()
        table_name = self.__class__.__name__.lower()
        columns = inspect.getmembers(self.__class__, lambda x: isinstance(x, property))
        columns = [c[0] for c in columns]
        columns_str = ", ".join([f"{c} TEXT" for c in columns])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {columns_str})"
        print(create_table_sql)
        cursor.execute(create_table_sql)
        self.connection.commit()

    def save(self):
        if not self.connection:
            print(f"Error: No database connection for class {self.__class__.__name__}")
            return None

        table_name = self.__class__.__name__.lower()
        primary_key = self.get_primary_key(table_name)
        if not primary_key:
            print(f"Error: Primary key not found for table {table_name}")
            return None

        # Überprüfen, ob der Eintrag bereits in der Datenbank vorhanden ist
        where_clause = f"{primary_key} = %s"
        params = (getattr(self, primary_key),)
        existing_entry = self.select_data(table_name, "*", where_clause, params)

        if existing_entry:
            # Eintrag existiert bereits, daher ein UPDATE durchführen
            columns = self.getColumns()
            set_clause = ", ".join(
                [f"{col} = %s" for col in columns if col != primary_key]
            )
            update_params = [
                getattr(self, col) for col in columns if col != primary_key
            ]
            update_params.append(getattr(self, primary_key))
            try:
                self.update_data(table_name, set_clause, where_clause, update_params)
            except mysql.connector.Error as e:
                print(f"Fehler bei der Update: {e}")
                return None
        else:
            # Eintrag existiert nicht, daher ein INSERT durchführen
            columns = self.getColumns()
            values = [getattr(self, c) for c in columns]
            try:
                self.insert_data(table_name, columns, values)
            except mysql.connector.Error as e:
                print(f"Fehler bei der Insert: {e}")
                return None

    def key(self, var):
        return str(var)

    def get_primary_key(self, table):
        # Funktion, um den Primärschlüssel der Tabelle zu erhalten
        query = f"SHOW KEYS FROM {table} WHERE Key_name = 'PRIMARY'"
        result = self.fetch_data(query)
        if result:
            primary_key_column = result[0][
                "Column_name"
            ]  # Spaltenname des Primärschlüssels
            return primary_key_column
        else:
            return None

    def load(self, id):
        if not self.connection:
            print(f"Error: No database connection for class {self.__class__.__name__}")
            return None

        table_name = self.__class__.__name__.lower()
        primary_key = self.get_primary_key(table_name)
        if not primary_key:
            print(f"Error: Primary key not found for table {table_name}")
            return None

        columns = "*"  # Alle Spalten auswählen
        where_clause = f"{primary_key} = %s"
        params = (id,)
        rows = self.select_data(table_name, columns, where_clause, params)

        if not rows:
            print(f"Error: No entry with ID {id} found in table {table_name}")
            return None

        row = rows[0]
        instance = self.__class__()
        for col_name, col_value in row.items():
            setattr(instance, col_name, col_value)

        return instance

    def delete_data_by_id(self, table, id_value):
        primary_key = self.get_primary_key(table)
        if not primary_key:
            print(f"Error: Primary key not found for table {table}")
            return

        query = f"DELETE FROM {table} WHERE {primary_key} = %s"
        self.execute_query(query, (id_value,))

    def delete(self):
        primary_key = self.get_primary_key(self.__class__.__name__.lower())
        if not primary_key:
            print("Error: Primary key not found for the table")
            return

        id_value = getattr(self, primary_key)
        if id_value is not None:
            query = f"DELETE FROM {self.__class__.__name__.lower()} WHERE {primary_key} = %s"
            self.execute_query(query, (id_value,))
            print(f"Record with {primary_key}={id_value} deleted.")
        else:
            print(f"Error: {primary_key} attribute not set for the instance.")

    def getColumns(self):
        columns = inspect.getmembers(self.__class__, lambda x: isinstance(x, property))
        return [c[0] for c in columns]
