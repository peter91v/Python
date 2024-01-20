from ..base.autopersistent import AutoPersistentController
from datetime import datetime as dt


class s102(AutoPersistentController):
    connection = None

    def __init__(
        self,
        datum: dt.date = None,
        realfeel: float = None,
        Temperature: float = None,
        updated: str = None,
        weather_forecast_id: int = None,
        zeit: dt.time = None,
    ):
        self._datum = datum
        self._realfeel = realfeel
        self._Temperature = Temperature
        self._updated = updated
        self._weather_forecast_id = weather_forecast_id
        self._zeit = zeit

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, value):
        self._datum = value

    @property
    def realfeel(self):
        return self._realfeel

    @realfeel.setter
    def realfeel(self, value):
        self._realfeel = value

    @property
    def Temperature(self):
        return self._Temperature

    @Temperature.setter
    def Temperature(self, value):
        self._Temperature = value

    @property
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, value):
        self._updated = value

    @property
    def weather_forecast_id(self):
        return self._weather_forecast_id

    @weather_forecast_id.setter
    def weather_forecast_id(self, value):
        self._weather_forecast_id = value

    @property
    def zeit(self):
        return self._zeit

    @zeit.setter
    def zeit(self, value):
        self._zeit = value
