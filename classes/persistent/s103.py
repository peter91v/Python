from ..base.autopersistent import AutoPersistentController
from datetime import datetime as dt


class s103(AutoPersistentController):
    connection = None

    def __init__(
        self,
        datum: dt.date = None,
        realfeel: float = None,
        temperature: float = None,
        updated: str = None,
        weather_forecast_id: int = None,
        zeit: dt.time = None,
    ):
        self._datum = datum
        self._realfeel = realfeel
        self._temperature = temperature
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
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

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
