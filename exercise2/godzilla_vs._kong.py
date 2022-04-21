movie_budget = float(input())
number_of_extras = int(input())
price_clothes_for_one_extra = float(input())

price_for_decor = movie_budget * 0.1
price_for_clothes = number_of_extras * price_clothes_for_one_extra

if number_of_extras > 150:
    price_for_clothes = price_for_clothes - (price_for_clothes * 0.1)

total_budget = price_for_decor + price_for_clothes
money_left = movie_budget - total_budget


if total_budget > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(total_budget - movie_budget):.2f} leva more.")

else:
    print(f"Action!")
    print(f"Wingard starts filming with {(money_left):.2f} leva left.")
