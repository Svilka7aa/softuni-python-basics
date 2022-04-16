price_for_practice = int(input())
price_for_kicks = price_for_practice - (price_for_practice * (40 / 100))
price_for_clothes = price_for_kicks - (price_for_kicks * (20 / 100))
price_for_ball =  price_for_clothes / 4
price_for_accessories = price_for_ball / 5

total = price_for_practice + price_for_kicks + price_for_clothes + price_for_ball + price_for_accessories

print(total)