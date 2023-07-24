import requests
import json

def currency_converter():
    print("Welcom to Zhou's currency converter!")
    print("Do you want to calculate the current rate or historical rate(Type 'C' for current or 'H' for history")
    user_choice = input()

    while user_choice != "H" and user_choice != "C":
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
print("Do you want to convert again?")
again_choice = input()
while True:
    if again_choice == "YES" or again_choice == "Y":
        currency_converter()
    else:
        break

print("Thank you for using Zhou's Currency Converter")