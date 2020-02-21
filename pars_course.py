import requests

url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
response = requests.get(url).json()
money_list = {}


def show_money():
    interest = ["EUR", "USD", "PLN", "RUB", "UAH", "AUD", "BLR"]  # TODO:универсальная кнопка для всех валют

    for item in list(response):
        if item['Cur_Abbreviation'] in interest:
            money = {item['Cur_Abbreviation']: item['Cur_OfficialRate']}
            money_list.update(money)
    return money_list
