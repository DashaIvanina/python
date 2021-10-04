#2
from requests import get, utils
from decimal import  *
from datetime import datetime

getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None

    rub = response[response.find('<Value>', response.find(val))+7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="')+6:response.find('"', response.find('Date="')+6)].split('.')
    day, mount, year = map(int, day_raw)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=mount, year=year)}"

print(currency_rates('EUR'))