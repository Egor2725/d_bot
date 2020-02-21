import requests


appid = "96b3571387d7b8e0d5b71b4a15a00029"
weather_values = []
city_name = 'минск'


def find_id(city_name):  # поиск id города
    city_id = 0
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': city_name, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    city_id = data['list'][0]['id']
    return city_id


def wheather_now(city_name):  # погода сейчас
    city_id = find_id(city_name)
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        weather_values = f"{(data['weather'][0]['description']).capitalize()}, {round(data['main']['temp'])}°"
        return weather_values



    except Exception as e:
        print("Exception (weather):", e)
        pass


# wheather_now("Брест")

def hourly_weather(city_name):  # почасовая погода, правый столбик
    weather_list = []
    city_id = find_id(city_name)
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        for i in data['list']:
            lis = f"{i['dt_txt']}  t {round(i['main']['temp'])}°. {(i['weather'][0]['description']).capitalize()}"
            weather_list.append(lis)
        return weather_list
    except Exception as e:
        print("Exception (forecast):", e)


hourly_weather(city_name)
