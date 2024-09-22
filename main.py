import requests
import json
import pyttsx3

city=input("Enter the Name of the city \n")

url=f"https://api.weatherapi.com/v1/current.json?key=your_api_key&q={city}"

r=requests.get(url) 
# print(r.text)
weatherdic=json.loads(r.text)
c=weatherdic["current"]["temp_c"]

engine = pyttsx3.init()
engine.say(f"Current Temperature of {city} is {c} degrees.")
engine.runAndWait()
