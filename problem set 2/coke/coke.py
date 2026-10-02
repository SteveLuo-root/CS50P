amount = 50
while amount > 0:
    print("amount due:", amount)
    coin = int(input("insert coin: "))
    if coin in [5, 10, 25]:
        amount -=coin

print("change owed:", -amount)
