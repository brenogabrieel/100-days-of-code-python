#Fazer o clear após o usuário digitar 'yes'
import os
import art

print(art.logo_blindauction)
print("Welcome to the secret auction program.")

name_bid = {}
high_bid = 0
should_end = False

while not should_end:
    name = input("What is your name?: ").lower()
    bid_price = int(input("What is your bid?: $"))
    name_bid[name] = bid_price
    if bid_price > high_bid:
        high_bid = bid_price
    others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if others == "no":
        should_end = True
    elif others == "yes":
        os.system('cls')
    else:
        print("Invalid input, ending the auction.")
        should_end = True
for name, bid in name_bid.items():
    if bid == high_bid:
        print(f"The winner is {name} with a bid of {high_bid}")