from ..base.autopersistent import AutoPersistentController
from datetime import datetime as dt
from mysql.connector.connection import MySQLConnection


class Sensors(AutoPersistentController):
    connection = None
    klass_name = None

    def __init__(
        self,
        StandortId: int = None,
        Text: str = None,
        ShortName: str = None,
        SensorId: str = None,
        Date: dt.date = None,
        time: dt.time = None,
        Temperature: float = None,
    ):
        self._DATE = Date
        self._SensorId = SensorId
        self._ShortName = ShortName
        self._StandortId = StandortId
        self._TEMPERATURE = Temperature
        self._Text = Text
        self._time = time

    def klass_name(self):
        return self.__class__.__name__.lower()

    @property
    def DATE(self):
        return self._DATE

    @property
    def StandortId(self):
        return self._StandortId

    @property
    def Text(self):
        return self._Text

    @property
    def ShortName(self):
        return self._ShortName

    @property
    def SensorId(self):
        return self._SensorId

    @property
    def time(self):
        return self._time

    @property
    def TEMPERATURE(self):
        return self._TEMPERATURE

    @StandortId.setter
    def StandortId(self, value):
        self._StandortId = value

    @Text.setter
    def Text(self, value):
        self._Text = value

    @ShortName.setter
    def ShortName(self, value):
        self._ShortName = value

    @SensorId.setter
    def SensorId(self, value):
        self._SensorId = value

    @DATE.setter
    def DATE(self, value):
        self._DATE = value

    @time.setter
    def time(self, value):
        self._time = value

    @TEMPERATURE.setter
    def TEMPERATURE(self, value):
        self._TEMPERATURE = value
