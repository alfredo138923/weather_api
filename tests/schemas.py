weather_api_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "coord": {
            "type": "object",
            "properties": {
                "lon": {
                    "type": "number"
                },
                "lat": {
                    "type": "number"
                }
            },
            "required": [
                "lon",
                "lat"
            ]
        },
        "weather": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "main": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                    },
                    "required": [
                        "description",
                    ]
                }
            ]
        },
        "main": {
            "type": "object",
            "properties": {
                "temp": {
                    "type": "number"
                },
                "feels_like": {
                    "type": "number"
                },
                "temp_min": {
                    "type": "number"
                },
                "temp_max": {
                    "type": "number"
                },
                "pressure": {
                    "type": "integer"
                },
                "humidity": {
                    "type": "integer"
                },
                "sea_level": {
                    "type": "integer"
                },
                "grnd_level": {
                    "type": "integer"
                }
            },
            "required": [
                "temp",
            ]
        },
        "visibility": {
            "type": "integer"
        },
        "wind": {
            "type": "object",
            "properties": {
                "speed": {
                    "type": "number"
                },
                "deg": {
                    "type": "integer"
                },
                "gust": {
                    "type": "number"
                }
            },
            "required": [
                "speed",
                "deg",
            ]
        },
        "sys": {
            "type": "object",
            "properties": {
                "country": {
                    "type": "string"
                },
                "sunrise": {
                    "type": "integer"
                },
                "sunset": {
                    "type": "integer"
                }
            },
            "required": [
                "sunrise",
                "sunset"
            ]
        },
        "timezone": {
            "type": "integer"
        },
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "cod": {
            "type": "integer"
        }
    },
    "required": [
        "main",
        "sys",
        "weather",
        "coord",
        "wind"
    ]
}
