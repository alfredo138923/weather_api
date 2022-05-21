from const import DEGREE_TYPES
from utils import unix_timestamp_to_readable_date, deg_to_compass
from datetime import datetime


def get_formatted_weather(api_response, units, location):

    temperature = api_response['main']['temp']

    if units == 'metric':
        temperature = '{} °{}'.format(temperature, DEGREE_TYPES['FAHRENHEIT']['symbol'])
    else:
        temperature = '{} °{}'.format(temperature, DEGREE_TYPES['CELCIUS']['symbol'])

    main = api_response['main']
    sys = api_response['sys']
    weather = api_response['weather'][0]
    coord = api_response['coord']
    wind_response = api_response['wind']

    humidity = main['humidity']

    sunrise = sys['sunrise']
    sunset = sys['sunset']

    sunrise = unix_timestamp_to_readable_date(sunrise)
    sunset = unix_timestamp_to_readable_date(sunset)
    compass_direction = deg_to_compass(wind_response['deg'])

    cloudiness = '{}'.format(weather['description'])
    pressure = '{} hPa'.format(main['pressure'])

    geo_coordinates = '[{}, {}]'.format(coord['lat'], coord['lon'])
    wind_speed = '{} m/s {}'.format(wind_response['speed'], compass_direction)

    data = {
        'location_name': location,
        'temperature': temperature,
        'wind': wind_speed,
        'cloudiness': cloudiness,
        'pressure': pressure,
        'humidity': humidity,
        'sunrise': sunrise.strftime('%H:%M'),
        'sunset': sunset.strftime('%H:%M'),
        'geo_coordinates': geo_coordinates,
        'requested_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    return data
