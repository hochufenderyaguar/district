from params import geocoder_params
import requests

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
response = requests.get(geocoder_api_server, params=geocoder_params)

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

geocoder_params1 = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": ','.join([toponym_longitude, toponym_lattitude]),
    "format": "json",
    "kind": "district"
}

response = requests.get(geocoder_api_server, params=geocoder_params1)
json_response = response.json()
print(json_response['response']["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]
      ["GeocoderMetaData"]["Address"]["Components"][5]['name'])
