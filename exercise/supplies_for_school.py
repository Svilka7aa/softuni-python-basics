price_packs_pen = 5.80
price_markers_packs = 7.20
price_liquid_litre = 1.20

number_packages_pens = int(input())
number_packages_markers = int(input())
liters_cleaning_liquid = int(input())
discount = int(input())

price_pens = number_packages_pens * price_packs_pen
price_markers = number_packages_markers * price_markers_packs
price_liquid = liters_cleaning_liquid * price_liquid_litre

price_sum = price_pens + price_markers + price_liquid

price_with_discount = price_sum - (price_sum * (discount / 100))

print(price_with_discount)
