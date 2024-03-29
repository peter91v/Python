import sqlite3
import mysql.connector


class DatabaseController:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.db_connection = None

    def connect(self):
        try:
            if self.db_connection is None:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
            else:
                self.connection = self.db_connection
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Verbindung zur Datenbank hergestellt")
        except mysql.connector.Error as e:
            print(f"Fehler bei der Verbindung zur Datenbank: {e}")
            return None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Verbindung zur Datenbank getrennt")

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.connection.commit()
                print("Abfrage erfolgreich ausgeführt")
        except mysql.connector.Error as e:
            print(f"Fehler beim Ausführen der Abfrage: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def fetch_data(self, query, params=None):
        rows = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                rows = cursor.fetchall()
            return rows
        except mysql.connector.Error as e:
            print(f"Fehler beim Abrufen der Daten: {e}")
            return None
        finally:
            cursor.close()

    def select_data(self, table, columns="*", where_clause=None, params=None):
        query = f"SELECT {columns} FROM {table}"
        if where_clause:
            query += f" WHERE {where_clause}"
        return self.fetch_data(query, params)

    def insert_data(self, table, columns, values):
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(values))})"
        self.execute_query(query, values)

    def delete_data(self, table, where_clause=None, params=None):
        query = f"DELETE FROM {table}"
        if where_clause:
            query += f" WHERE {where_clause}"
        self.execute_query(query, params)

    def update_data(self, table, set_clause, where_clause=None, params=None):
        query = f"UPDATE {table} SET {set_clause}"
        if where_clause:
            query += f" WHERE {where_clause}"
        self.execute_query(query, params)

    def get_columns(self, table_name, data_type=False):
        if data_type:
            result = self.select_data(
                "INFORMATION_SCHEMA.COLUMNS",
                "COLUMN_NAME, DATA_TYPE",
                f"TABLE_NAME='{table_name}'",
            )
        else:
            result = self.select_data(
                "INFORMATION_SCHEMA.COLUMNS",
                "COLUMN_NAME",
                f"TABLE_NAME='{table_name}'",
            )
        if result:
            return result
        else:
            return None
