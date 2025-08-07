import requests

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "643edc50fddd59596c9720c56229408d"

weather_params = {
    "lat":-1.292066,
    "lon":36.821945,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get(OMW_Endpoint, params=weather_params)
print(response.json())
