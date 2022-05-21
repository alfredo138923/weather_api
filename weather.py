from const import DEGREE_TYPES
from utils import unix_timestamp_to_readable_date, deg_to_compass
from datetime import datetime


def get_formatted_weather(api_response, units, location):

    temperature = api_response['main']['temp']

    if units == 'metric':
        temperature = '{} °{}'.format(temperature, DEGREE_TYPES['FAHRENHEIT']['symbol'])
    else:
        temperature = '{} °{}'.format(temperature, DEGREE_TYPES['CELCIUS']['symbol'])

    humidity = '{}'.format(api_response['main']['humidity'])

    sunrise = api_response['sys']['sunrise']
    sunset = api_response['sys']['sunset']

    sunrise = unix_timestamp_to_readable_date(sunrise)
    sunset = unix_timestamp_to_readable_date(sunset)

    cloudiness = '{}'.format(api_response['weather'][0]['description'])
    pressure = '{} hPa'.format(api_response['main']['pressure'])

    geo_coordinates = '[{}, {}]'.format(api_response['coord']['lat'], api_response['coord']['lon'])

    wind_speed = '{} m/s {}'.format(api_response['wind']['speed'], deg_to_compass(api_response['wind']['deg']))

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
