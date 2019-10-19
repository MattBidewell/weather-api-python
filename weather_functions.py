# Weather


from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring #xml
from urllib.parse import quote #URL encoder
import requests
import json
import collections

base_url="http://weather.service.msn.com/find.aspx?src=outlook&weadegreetype=(c)&culture=(en-us)&weasearchstr="

default_timeout=10000

def get_weather(LOC): 
    json_response = get_request(LOC)
    weather_obj = handle_response(json_response)
    return weather_obj

def get_request(LOC):
    print("sending request for: " + LOC)
    encoded_loc = quote(LOC)
    print(base_url+encoded_loc)
    response = requests.get(base_url+encoded_loc)
    
    if(response.status_code < 400) :
        unformatted_data = response.text
        json_data = bf.data(fromstring(unformatted_data))
        return json_data
    else :
        print("Error sending request " + response.status_code)

def handle_response(data):
    # weatherObj = json.loads(json.dumps(data))
    filteredObj = data['weatherdata']['weather']

    if isinstance(filteredObj, list):
       weatherObj = filteredObj[0]
    else :
        weatherObj = filteredObj

    todaysWeather = handle_weather_forecast(weatherObj['forecast'][1])
    tomorrowsWeather = handle_weather_forecast(weatherObj['forecast'][2])
    twoDaysTimeWeather = handle_weather_forecast(weatherObj['forecast'][3])
    threeDaysTimeWeather = handle_weather_forecast(weatherObj['forecast'][4])

    response = {
        0: todaysWeather,
        1: tomorrowsWeather,
        2: twoDaysTimeWeather,
        3: threeDaysTimeWeather
    }

    return response

def handle_weather_forecast(weatherBlock):
    weather = weatherBlock['@skytextday']
    high = weatherBlock['@high']
    low = weatherBlock['@low']
    percipitation = weatherBlock['@precip']
    day = weatherBlock['@day']
    date = weatherBlock['@date']

    return {"weather": weather, "high": high, "low": low, "percipitation": percipitation, "day": day, "date": date}