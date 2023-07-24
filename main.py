import requests
import json

def currency_converter():
    print("Welcome to Zhou's currency converter!")
    print("Do you want to see the supported currencies? 'Y' for yes or 'NO' for no")
    supported_cur = input().upper()
    if supported_cur == "Y":
        print('''
    "AUD": "Australian Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Renminbi Yuan",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "GBP": "British Pound",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "ISK": "Icelandic Króna",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Złoty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "USD": "United States Dollar",
    "ZAR": "South African Rand"
        ''')
    else:
        pass

    print("Do you want to calculate the current rate or historical rate(Type 'C' for current or 'H' for history")
    user_choice = input().upper()

    while (user_choice != "H" and user_choice != "C") and user_choice != "L":
        print("Invalid input(Type 'C' for current or 'H' for history")
        user_choice = input()

    if user_choice == "C":
        print("Which currency do you want to exchange from (Type the three letter code ex.USD EUR)")
        exchange_from = input().upper()
        print("Which currency do you want to exchange to")
        exchange_to = input().upper()
        print(f"How much {exchange_from} do you want to convert?")
        exchange_amount = float(input())
        r = requests.get(f"https://api.frankfurter.app/latest?amount={exchange_amount}&from={exchange_from}&to{exchange_to}")
        python_converted = json.loads(r.content)
        converted_rate = round(python_converted["rates"][exchange_to], 4)
        print(f"Your {exchange_amount} {exchange_from} converted to {converted_rate} {exchange_to}.")
    elif user_choice == "H":
        print("Enter the historical date you want to convert in YYYY-MM-DD")
        date_initial = input()
        split_date = date_initial.split("-")
        print("Which currency do you want to exchange from (Type the three letter code ex.USD EUR)")
        exchange_from = input().upper()
        print("Which currency do you want to exchange to")
        exchange_to = input().upper()
        print(f"How much {exchange_from} do you want to convert?")
        exchange_amount = float(input())
        r = requests.get(f"https://api.frankfurter.app/{split_date[0]}-{split_date[1]}-{split_date[2]}?{exchange_amount}&from={exchange_from}&to{exchange_to}")
        python_converted = json.loads(r.content)
        exchange_rate = python_converted["rates"][exchange_to]
        converted_rate = round(exchange_rate * exchange_amount, 4)
        print(f"Your {exchange_amount} {exchange_from} converted to {converted_rate} {exchange_to}.")

currency_converter()

print("Do you want to convert again? Type 'YES' or 'Y'")
again_choice = input().upper()

while again_choice != "YES" or again_choice != "Y":
    print("Invalid input, try again")
    again_choice = input().upper()
while True:
    if again_choice == "YES" or again_choice == "Y":
        currency_converter()
    else:
        break

print("Thank you for using Zhou's Currency Converter")