import requests

url = "https://api.open-meteo.com/v1/forecast"

yesilpinar_req = {
    "latitude": 41.07255,
    "longitude": 28.92391,
    "current_weather": True
}

gemlik_req = {
    "latitude": 40.43280,
    "longitude": 29.15617,
    "current_weather": True
}

antalya_req = {
    "latitude": 36.89300,
    "longitude": 30.70376,
    "current_weather": True
}

yesilpinar_json = requests.get(url, params=yesilpinar_req).json()
gemlik_json = requests.get(url, params=gemlik_req).json()
antalya_json = requests.get(url, params=antalya_req).json()

yesilpinar_data = yesilpinar_json['current_weather']
gemlik_data = gemlik_json['current_weather']
antalya_data = antalya_json['current_weather']

print(f"""
YESILPINAR: 
time: {yesilpinar_data['time']}
temperature: {yesilpinar_data['temperature']}
windspeed: {yesilpinar_data['windspeed']}

GEMLIK:
time: {gemlik_data['time']}
temperature: {gemlik_data['temperature']}
windspeed: {gemlik_data['windspeed']}

ANTALYA:
time: {antalya_data['time']}
temperature: {antalya_data['temperature']}
windspeed: {antalya_data['windspeed']}
""")
