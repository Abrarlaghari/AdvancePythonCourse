import requests
from threading import Thread, Lock
from datetime import datetime
import globals

lock = Lock()

class WeatherGetter(Thread):
    def __init__(self, city, sem):
        Thread.__init__(self)
        self._city = city
        self._sem = sem
    def run(self):
        self._sem.acquire()
        try:
            report = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self._city}&units=metric&APPID=957d663a2296945e39a56609740a2548')
            data = report.json()
            self.temperature = data['main']['temp']
            print(f'Temperature in {self._city} is {self.temperature}')
            lock.acquire()
            globals.cities_data[self._city] = [f"Temperature: {self.temperature}", f"TimeStamp: {datetime.now()}"]
        except Exception as e:
            print(f'Error occured: {e}')
            lock.acquire()
            globals.cities_data[self._city] = [f"Temperature: null", f"TimeStamp: {datetime.now()}"]
        finally:
            lock.release()
        self._sem.release()

if __name__ == '__main__':
    pass
