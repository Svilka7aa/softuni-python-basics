price_shirt = float(input())
target = float(input())

price_shorts = price_shirt * 0.75
price_socks = price_shorts * 0.2
price_shoes = 2 * (price_shirt + price_shorts)

total = price_shirt + price_shorts + price_socks + price_shoes\

price_with_discount = total - total * 0.15

if price_with_discount >= target:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {price_with_discount:.2f} lv.")

else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {target - price_with_discount:.2f} lv. more.")