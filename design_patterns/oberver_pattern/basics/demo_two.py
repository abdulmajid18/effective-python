from abc import ABC, abstractmethod
from typing import List

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass


# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


# Concrete Subject: WeatherStation
class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


# Concrete Observers
class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(
            f"Current Conditions: Temperature = {temperature}°C, Humidity = {humidity}%, Pressure = {pressure}hPa"
        )


class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperatures = []
        self._humidities = []
        self._pressures = []

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperatures.append(temperature)
        self._humidities.append(humidity)
        self._pressures.append(pressure)

        avg_temp = sum(self._temperatures) / len(self._temperatures)
        avg_humidity = sum(self._humidities) / len(self._humidities)
        avg_pressure = sum(self._pressures) / len(self._pressures)

        print(
            f"Statistics: Avg Temperature = {avg_temp:.2f}°C, Avg Humidity = {avg_humidity:.2f}%, "
            f"Avg Pressure = {avg_pressure:.2f}hPa"
        )


# Main Program
if __name__ == "__main__":
    # Create the WeatherStation (Subject)
    weather_station = WeatherStation()

    # Create Displays (Observers)
    current_conditions_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()

    # Register Displays to the WeatherStation
    weather_station.register_observer(current_conditions_display)
    weather_station.register_observer(statistics_display)

    # Simulate Weather Data Changes
    weather_station.set_measurements(25.0, 65.0, 1013.0)
    weather_station.set_measurements(26.5, 70.0, 1012.5)
    weather_station.set_measurements(24.0, 60.0, 1014.0)

    # Remove an Observer
    weather_station.remove_observer(statistics_display)

    # Simulate Another Weather Data Change
    weather_station.set_measurements(23.0, 55.0, 1015.0)