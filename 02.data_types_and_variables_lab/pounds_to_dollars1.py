import requests


def convert_gbp_to_usd(amount):
    response = requests.get('https??api.exchangerate-api.com/v4/latest/GBP')
    exchange_rates = response.json()['rates']
    usd_rate = exchange_rates['USD']
    usd_amount = amount * usd_rate

    return usd_amount


pounds = int(input('Enter an amount of pounds:'))
us_dollars = convert_gbp_usd()
