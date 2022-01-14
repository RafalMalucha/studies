amount = int(input("Enter the amount in PLN:  "))
if amount >= 0:
    coin5 = amount // 5
    coin2 = (amount - (coin5 * 5)) // 2
    coin1 = amount - ((coin5 * 5) + (coin2 * 2))
    
    print(f"The amount of PLN {amount} in coins:")
    print(f"5 zł – {coin5}")
    print(f"2 zł – {coin2}")
    print(f"1 zł – {coin1}")

else:
    print("excuse me, but why do you want to calculate your debt in coins?")

