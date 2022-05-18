import requests
from datetime import datetime

API_KEY = 'd35902742cd01cb37ebdcb84'
url = 'https://v6.exchangerate-api.com/v6/d35902742cd01cb37ebdcb84/latest/USD'
# 'https://app.exchangerate-api.com/dashboard/confirmed'

# Fetching exchange rates
response = requests.get(url)
data = response.json()

# Grabbing just the prices from dictionary
prices = (data['conversion_rates'])

# Grabbing just the currency names from dictionary
currencies = list(prices.keys())

# Grabbing time and converting to readable time
unix_time = data['time_last_update_unix']
time = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d')

print('\nCurrency Converter\n')

# User inputs
list = input('Would you like to see a list of currencies?(Y/N): ').upper()
if list == 'Y':print(currencies)
currency = input('Which currency would you like to convert?: ').upper()
convert = input('What would you like to convert the currency to?: ').upper()
amount = int(input(f'How many {currency} would you like to convert?: '))

# Checking to see if user inputs match the currencies in dictionary
if currency and convert in currencies:
    # Defining price of currencies user wants converted
    currency_price = prices[currency]
    convert_price = prices[convert]

    conversion = currency_price * convert_price * amount

    print(f"\nAt current exchange rates {amount} {currency} converts to {conversion} {convert}")
    print(f'Rates last updated {time}')
else:
    print('not found')
