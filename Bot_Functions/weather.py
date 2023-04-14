from Bot_Functions import places
from dotenv import load_dotenv
import os
import requests
import json

def find_weather(location, units):
    load_dotenv()
    api_key = os.getenv('WEATHER_TOKEN')
    location = places.get_location(location)
    lat = location[0]
    lon = location[1]

    if location == "invalid":
        return "Invalid Location"
    # base_url variable to store url
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key + "&units=" + units

    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    print(response)
    report = response.json()

    if units == 'imperial':
        return ("Temperature: "+ str(report['main']['temp']) + "°F"+ "\n" + 
            "Feels like: "+ str(report['main']['feels_like']) + "°F"+ "\n" + 
            "Minimum temperature: " + str(report['main']['temp_min']) + "°F"+ "\n" +
            "Maximum temperature: " + str(report['main']['temp_max']) + "°F")
    
    if units == 'metric':
        return ("Temperature: "+ str(report['main']['temp']) + "°C"+ "\n" + 
            "Feels like: "+ str(report['main']['feels_like']) + "°C"+ "\n" + 
            "Minimum temperature: " + str(report['main']['temp_min']) + "°C"+ "\n" +
            "Maximum temperature: " + str(report['main']['temp_max']) + "°C")
    
    if units == 'standard':
        return ("Temperature: "+ str(report['main']['temp']) + "K"+ "\n" + 
            "Feels like: "+ str(report['main']['feels_like']) + "K"+ "\n" + 
            "Minimum temperature: " + str(report['main']['temp_min']) + "K"+ "\n" +
            "Maximum temperature: " + str(report['main']['temp_max']) + "K")