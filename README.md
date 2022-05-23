# Alfredo Marcillo
## Weather API

## Instructions

Requires [Python3](https://www.python.org) v3.5+ to run.

Install Pyenv packaging tool.

```sh
pip install --user pipenv
```

## Redis
Read the following the instructions to install Redis according your OS.
https://redis.io/docs/getting-started/installation/

Clone the repository:
```sh
git clone https://github.com/alfredo138923/weather_api.git
cd weather_api
```

Install the dependencies using pipenv:
```sh
pipenv sync
```

Activate the enviroment:
```sh
pipenv shell
```

Create a *.secrets.toml* file in the root directory to store all the sensitive data with the following format to connect to openweathermap:

```toml
[default]
TOKEN = 'my-very-secret token'
OPENWEATHER_API_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
```

Run tests from root directory:
```sh
python -m pytest -s tests
```

Run the Flask server:
```sh
flask run
```

API call.

HTTP Method: GET

```sh
http://localhost:8050/get_current_weather/
```

Parameters:

| parameter | type   | required | description                                                |
|-----------|--------|----------|------------------------------------------------------------|
| country   | string | true     | Code of the country. [Codes](https://en.wikipedia.org/w/index.php?title=ISO_3166-1#Officially%20assigned%20code%20element)                                      |
| city      | string | true     | Name of the city                                           |                            |
| units     | string | false    | Units of measurement: standard, metric (default: standard) |

## License

GNU General Public License v3.0
