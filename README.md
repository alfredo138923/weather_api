# Alfredo Marcillo
## Weather API

## Instructions

Requires [Python3](https://www.python.org) v3.5+ to run.

Install Pyenv packaging tool.

```sh
pip install --user pipenv
```

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

Run the Flask server:
```sh
flask run
```

## License

GNU General Public License v3.0
