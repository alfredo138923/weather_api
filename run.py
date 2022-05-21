import requests
from dynaconf import FlaskDynaconf
from flask import Flask, request
from weather import get_formatted_weather
from flask_caching import Cache

app = Flask(__name__)
FlaskDynaconf(app)
cache = Cache(app)  # Initialize Cache

WEATHER_ENDPOINT = app.config['OPENWEATHER_API_ENDPOINT']


@app.route('/get_current_weather/', methods=['GET'])
@cache.cached(timeout=120, query_string=True)
def get_current_weather():
    country_code = request.args.get('country', '').upper()
    city_code = request.args.get('city', '').title()
    units = request.args.get('units', '').lower()

    location = '{}, {}'.format(city_code, country_code)

    params = {
        'q': location,
        'appid': app.config['TOKEN'],
        'units': units
    }

    response = requests.get(WEATHER_ENDPOINT, params=params)

    response = response.json()

    data = get_formatted_weather(response, units, location)

    return data
