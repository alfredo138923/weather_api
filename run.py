from flask import Flask, request
from dynaconf import FlaskDynaconf
import requests

app = Flask(__name__)

FlaskDynaconf(app)

WEATHER_ENDPOINT = app.config['OPENWEATHER_API_ENDPOINT']

DEGREE_TYPES = {
    'FAHRENHEIT': {
        'symbol': 'C'
    },
    'CELCIUS': {
        'symbol': 'F'
    }
}


@app.route('/get_current_weather/', methods=['GET'])
def get_current_weather():
    country_code = request.args.get('country', '').lower()
    city_code = request.args.get('city', '').lower()
    units = request.args.get('units', '').lower()

    location = '{},{}'.format(city_code, country_code)

    params = {
        'q': location,
        'appid': app.config['TOKEN'],
        'units': units
    }

    response = requests.get(WEATHER_ENDPOINT, params=params)

    response = response.json()

    return response
