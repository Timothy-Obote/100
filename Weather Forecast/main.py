import requests

import os
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "643edc50fddd59596c9720c56229408d"

account_sid = "AC8d433276b8644e9491215ac5c34deccd"
auth_token = "871fe7efb4a2240edccd3bb126b95394"

weather_params = {
    "lat":-1.292066,
    "lon":36.821945,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = (response.json())
print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False

for hour_data in weather_data["list"]:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code) < 700 :
        will_rain = True
if will_rain:
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
    body="It will rain ,bring an umbrella",
    from_="+18566060195",
    to="+18566060195",
)

print(message.status)
