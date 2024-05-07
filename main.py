import googlemaps
from datetime import datetime
import time
import csv


def go():
    gmaps = googlemaps.Client(key='YOUR-TOKEN-HERE')
    from_point = "Direction here"
    to_point = "Direction here"

    for x in range(24*7):
        now = datetime.now()
        print('\nGetting measures {}'.format(now))

        res = gmaps.directions(from_point, to_point, mode="driving", departure_time=now)
        temps_anada = res[0]['legs'][0]['duration']['text']
        time.sleep(1)
        res = gmaps.directions(to_point, from_point, mode="driving", departure_time=now)
        temps_tornada = res[0]['legs'][0]['duration']['text']

        print('Temps anada: {}'.format(temps_anada))
        print('Temps tornada: {}'.format(temps_tornada))
        twrite = [datetime.strftime(now, '%d/%m/%Y %H:%M:%S'), temps_anada, temps_tornada]
        with open("results.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(twrite)

        time.sleep(62) # 1 hour


if __name__ == '__main__':
    go()

