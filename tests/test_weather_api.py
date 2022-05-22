from config import settings
import requests
from jsonschema import validate

from tests.schemas import weather_api_schema

OPENWEATHER_API_ENDPOINT = settings['DEFAULT']['OPENWEATHER_API_ENDPOINT']
OPENWEATHER_API_TOKEN = settings['DEFAULT']['TOKEN']


def test_weather_api():
    """
    Check weather API availability
    :return:
    """

    location = 'montreal, CA'

    params = {
        'q': location,
        'appid': OPENWEATHER_API_TOKEN,
        'units': 'metrics'
    }

    response = requests.get(OPENWEATHER_API_ENDPOINT, params)

    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    validate(instance=response.json(), schema=weather_api_schema)

