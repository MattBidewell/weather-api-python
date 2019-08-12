# Weather


import requests

default_lang="en-US"
default_timeout=10000
default_degree_type="c"
base_url="http://weather.service.msn.com/find.aspx"

example_url="http://weather.service.msn.com/find.aspx?src=outlook&weadegreetype=(c)&culture=(en-us)&weasearchstr=borehamwood"

def get_request(URL, PARAMS):
    print("sending request to" + url)
    response = requests.get(url = URL, params = PARAMS)
    data = response.json()
    return handle_response(data)

def handle_response(data):
    #todoS




#findUrl + '?src=outlook&weadegreetype=' + (''+degreeType) + '&culture=' + (''+lang) + '&weasearchstr=' + search;