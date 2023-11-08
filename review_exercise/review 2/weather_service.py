import requests
import time
import json
from threading import Semaphore

from weatherclass import WeatherGetter
import globals

def main():
    CITIES = ['Athlone', 'Dublin', 'Galway', 'Belfast', 'Toronto', 'Cork', 'Budapest', 'Kista']
    threads = []
    sem = Semaphore(5)
    start = time.time()
    for _ in CITIES:
        threads.append(WeatherGetter(_, sem))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print(f'Total time taken {end-start} seconds')
    print(globals.cities_data)

    with open('weather.txt', 'w') as fil:
        fil.write(json.dumps(globals.cities_data))

if __name__ == '__main__':
    main()
