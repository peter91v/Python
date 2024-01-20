import base.databasecontroller as DBController
from datetime import date, timedelta

# file erstellen
# imports
#
# init erstellen bekommt eine liste {'COLUMN_NAME': 'datum', 'DATA_TYPE': 'date'}
# setter
# getter
# generet


class AutoPersistentGenerator:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.class_definition = []

    def CreateFile(self, Columns):
        file_path = f"{self.path}/{self.name.lower()}.py"
        try:
            # Die Datei im Schreibmodus öffnen
            with open(file_path, "w") as file:
                # Inhalt in die Datei schreiben (falls vorhanden)
                self.GenerateClass(Columns)
                # file.write(self.content)
                for class_def in self.class_definition:
                    file.write("%s\n" % class_def)
            print(f"Die Datei {self.name} wurde erfolgreich erstellt.")
        except Exception as e:
            print(f"Fehler beim Erstellen der Datei {self.name}: {e}")

    def AddImports(self):
        """Fügt den Imports von DBController und date hinzu."""
        return "from ..base.autopersistent import AutoPersistentController \nfrom datetime import datetime as dt\n\n"

    def GenerateClass(self, Columns):
        self.class_definition.append(self.AddImports())
        self.class_definition.append(f"class {self.name}(AutoPersistentController):")
        self.class_definition.append(f"    connection = None")
        self.class_definition.append("    def __init__(")
        self.class_definition.append("        self,")
        self.AddColumns(Columns)
        self.GenereteGetterAndSetter(Columns)

    def AddColumns(self, Columns):
        """Adds class variables for each column in the given dictionary."""
        colname = ""
        for col in Columns:
            colname = col["COLUMN_NAME"]
            if col["DATA_TYPE"] == "date":
                column_type = "dt.date"
            if col["DATA_TYPE"] == "varchar" or col["DATA_TYPE"] == "varchar2":
                column_type = "str"
            if col["DATA_TYPE"] == "time":
                column_type = "dt.time"
            if col["DATA_TYPE"] == "float":
                column_type = "float"
            if col["DATA_TYPE"] == "int":
                column_type = "int"
            class_variable = f"        {colname}: {column_type} = None,"
            self.class_definition.append(class_variable)
        self.class_definition.append("    ):")
        for col in Columns:
            colname = col["COLUMN_NAME"]
            self.class_definition.append(f"        self._{colname} = {colname}")

    def GenereteGetterAndSetter(self, Columns):
        colname = ""
        for col in Columns:
            colname = col["COLUMN_NAME"]
            self.class_definition.append(
                f"    @property\n    def {colname}(self):\n        return self._{colname}\n"
            )
            self.class_definition.append(
                f"    @{colname}.setter\n    def {colname}(self, value):\n        self._{colname} = value\n"
            )
