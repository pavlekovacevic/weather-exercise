import requests
import datetime
import sys

if (len(sys.argv) != 3):
    print("Please enter a city and country code.")
    sys.exit()
else:
    city = sys.argv[1]
    country_code = sys.argv[2]

r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&appid=0c478573a9d2870dace7de185bc54de5&units=metric")
response = r.json()

print("The coordinates of " + city + " are " + str(response['coord']['lon']) + ", " + str(response['coord']['lat']) + ".")
print("The current weather description is: " + response['weather'][0]['description'] + ".")
print("The temperature is " + str(response['main']['temp']) + " degrees Celsius.")
print("The weather feels like " + str(response['main']['feels_like']) + " degrees Celsius.")
print("The sun rises at " + str(datetime.datetime.fromtimestamp((response['sys']['sunrise']))) + " and sets at " + str(datetime.datetime.fromtimestamp((response['sys']['sunset']))) + ".") 
print("The pressure is " + str(response['main']['pressure']) + "mb and the humidity is " + str(response['main']['humidity']) + ".")