import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_NUMBER")

# Define the OpenWeather API URL and other parameters
URL = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = -10.996060 # Nairobi latitude
MY_LON = 26.761677 # Nairobi longitude
COUNT = 4  # Number of forecasts to retrieve



# Parameters for the API request
PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": COUNT,
}

# Make a request to the OpenWeather API
response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()  # Check for errors in the response
data = response.json()  # Parse the response JSON data

# Check if it will rain based on weather conditions
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:  # Weather codes below 700 indicate rain
        will_rain = True



# Output the result
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to not rain today. Dont bring an ☂️",
    from_= twilio_number,
    to= my_number
    )
else:
    print("No rain expected")