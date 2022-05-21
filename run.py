import requests
from dynaconf import FlaskDynaconf
from flask import Flask, request
from weather import get_formatted_weather

app = Flask(__name__)

FlaskDynaconf(app)

WEATHER_ENDPOINT = app.config['OPENWEATHER_API_ENDPOINT']


@app.route('/get_current_weather/', methods=['GET'])
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
