# 🌧 Rain Alert Notifier (Python + Twilio)

This is a simple Python script that checks the weather forecast using the [OpenWeatherMap API](https://openweathermap.org/api) and sends an SMS alert via [Twilio](https://www.twilio.com/) if rain is expected in the next few hours.

---

## 🚀 Features

- Fetches weather forecast for Nairobi, Kenya using OpenWeatherMap.
- Checks if rain is expected in the next 4 forecasted time blocks.
- Sends an SMS alert using Twilio if rain is detected.

---
🧠 How It Works
The script calls the OpenWeatherMap API to get a 5-day weather forecast.

It checks the next 4 forecast blocks (each ~3 hours apart).

If the weather condition code is below 700, it predicts precipitation (rain/snow).

If rain is expected, it sends an SMS alert using Twilio.


 📦 Requirements

Make sure you have Python 3.7+ installed.

Install required packages using:

