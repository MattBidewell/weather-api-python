# Weather


from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from urllib.parse import quote
from json import dumps

import requests

base_url="http://weather.service.msn.com/find.aspx?src=outlook&weadegreetype=(c)&culture=(en-us)&weasearchstr="

default_timeout=10000



def run(LOC): 
    json_response = get_request(LOC)
    weather_obj = handle_response(json_response)
    return print(weather_obj)

def get_request(LOC):
    print("sending request to: " + LOC)
    encoded_loc = quote(LOC)
    print(base_url+encoded_loc)
    response = requests.get(base_url+encoded_loc)
    
    if(response.status_code == 200) :
        unformatted_data = response.text
        json_data = bf.data(fromstring(unformatted_data))
        return json_data
    
def handle_response(data):
    print(data)
    return "nothing"

run("London")