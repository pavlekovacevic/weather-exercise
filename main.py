import requests
import datetime 

city = "London"
country_code = "GB"

r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&appid=0c478573a9d2870dace7de185bc54de5")
response = r.json()

print("The coordinates of " + city + " are " + str(response['coord']['lon']) + ", " + str(response['coord']['lat']) + ".")
print("The current weather description is: " + response['weather'][0]['description'] + ".")
print("The temperature is " + str(response['main']['temp'] - 273.15) + " degrees Celsius.")
print("The weather feels like " + str(response['main']['feels_like'] - 273.15) + " degrees Celsius.")
print("The sun rises at " + str(datetime.datetime.fromtimestamp((response['sys']['sunrise']))) + " and sets at " + str(datetime.datetime.fromtimestamp((response['sys']['sunset']))) + ".") 
print("The pressure is "+ str(response['main']['pressure']) + "mb and the humidity is " + str(response['main']['humidity']) + ".")