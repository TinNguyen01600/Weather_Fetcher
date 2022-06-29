from urllib import response
import requests
API_KEY = "b92a75a142d591e7c8c6381e8311c403"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL} ? appid = {API_KEY} & q = {city}"   # Embed var and expressions inside of a string
# appid and q are query parameters
response = requests.get(request_url)    # send a get request to url
# response contains info associate with our city