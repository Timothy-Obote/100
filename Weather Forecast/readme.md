# 🌧 Rain Alert Notifier (Python + Twilio)

A simple Python script that checks the weather forecast using the [OpenWeatherMap API](https://openweathermap.org/api) and sends an SMS alert via [Twilio](https://www.twilio.com/) if rain is expected in the next few hours.

---

## 🚀 Features

- Retrieves weather forecast for Nairobi, Kenya.
- Analyzes the next 4 forecasted time blocks (~12 hours).
- Sends SMS notifications if rain is likely.

---
🧠 How It Works
The script calls the OpenWeatherMap API to get a 5-day weather forecast.

It checks the next 4 forecast blocks (each ~3 hours apart).

If the weather condition code is below 700, it predicts precipitation (rain/snow).

If rain is expected, it sends an SMS alert using Twilio.
----
## 📦 Requirements

- Python 3.7 or higher

Install the required packages:

```bash
pip install requests twilio
🔧 Configuration
Edit the script to include your credentials:

python
Copy
Edit
# Weather API Key (get from https://openweathermap.org)
api_key = "your_openweathermap_api_key"

# Twilio credentials (get from https://twilio.com/console)
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"

# Phone numbers
from_ = "+Your_Twilio_Number"
to = "+Your_Verified_Recipient_Number"
💡 Best Practice: Use environment variables or a .env file to manage your secrets. You can load them with python-dotenv.



Edit
