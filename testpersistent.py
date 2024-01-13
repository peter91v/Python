import unittest
from datetime import datetime
from classes.persistent.sensor import Sensors


class TestSensors(unittest.TestCase):
    def setUp(self):
        self.db_connection = None

    def test_constructor(self):
        s = Sensors(
            ID=1,
            Bezeichnung="Sensor 1",
            Bezeichnungkurz="S1",
            SensorID="ABC123",
            Date=datetime.date(2021, 1, 1),
            Time=datetime.datetime(2021, 1, 1, 12, 0, 0),
            Temperature=20.0,
            db_connection=self.db_connection,
        )
        self.assertEqual(s.StandortId, 1)
        self.assertEqual(s.Text, "Sensor 1")
        self.assertEqual(s.ShortName, "S1")
        self.assertEqual(s.SensorId, "ABC123")
        self.assertEqual(s.Date, datetime.date(2021, 1, 1))
        self.assertEqual(s.Time, datetime.datetime(2021, 1, 1, 12, 0, 0))
        self.assertEqual(s.Temperature, 20.0)

    def test_setters(self):
        s = Sensors(
            ID=1,
            Bezeichnung="Sensor 1",
            Bezeichnungkurz="S1",
            SensorID="ABC123",
            Date=datetime.date(2021, 1, 1),
            Time=datetime.datetime(2021, 1, 1, 12, 0, 0),
            Temperature=20.0,
            db_connection=self.db_connection,
        )
        s.StandortId = 2
        s.Text = "Sensor 2"
        s.ShortName = "S2"
        s.SensorId = "DEF456"
        s.Date = datetime.date(2021, 1, 2)
        s.Time = datetime.datetime(2021, 1, 2, 12, 0, 0)
        s.Temperature = 25.0
        self.assertEqual(s.StandortId, 2)
        self.assertEqual(s.Text, "Sensor 2")
        self.assertEqual(s.ShortName, "S2")
        self.assertEqual(s.SensorId, "DEF456")
        self.assertEqual(s.Date, datetime.date(2021, 1, 2))
        self.assertEqual(s.Time, datetime.datetime(2021, 1, 2, 12, 0, 0))
        self.assertEqual(s.Temperature, 25.0)


if __name__ == "__main__":
    unittest.main()
