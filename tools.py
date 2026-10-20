
from datetime import datetime
import requests 

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_city_Weather(city):

    url=f"https://wttr.in/{city}?format=3"
    response=requests.get(url,timeout=10)
    return response.text;

def get_my_city():
    return "Jaipur"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local date and time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_city_Weather",
            "description":"Get the current weather of a given City",
            "parameters":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"The city whose weather we are finding."
                    }
                },
                "required":["city"]
            }
        }
    },
        {
        "type": "function",
        "function": {
            "name": "get_my_city",
            "description": "Get my current city.It finds the city where Im currently in.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
    
]

FUNCTION_NAME_TO_FUNCTION_MAP = {

    "get_current_time": get_current_time,
    "get_city_Weather": get_city_Weather,
    "get_my_city": get_my_city,

}
