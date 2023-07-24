import requests
import json

exchange_rate_cache = {} #to improve efficiency on previously converted rates

print("Do you want to calculate the current rate or historical rate(Type 'C' for current or 'H' for history")
user_choice = input()

if user_choice == "C":
    print("Which currency do you want to exchange from (Type the three letter code ex.USD EUR)")
    exchange_from = input()
    print("Which currency do you want to exchange to")
    exchange_to = input()
    print("How much money do you have?")
    exchange_amount = float(input())
    r = requests.get(f"https://api.frankfurter.app/latest?amount={exchange_amount}&from={exchange_from}&to{exchange_to}")

