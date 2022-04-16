budged = int(input())
season = input()
fishers_count = int(input())

ship_price = 0

# Ако групата е до 6 човека включително  -  отстъпка от 10%;
# Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# Ако групата е от 12 нагоре  -  отстъпка от 25%.

if season == "Spring":
    ship_price = 3000
    if fishers_count <= 6:
        ship_price -= ship_price * 0.1
    elif 7 <= fishers_count <= 11:
        ship_price -= ship_price * 0.15
    elif 12 <= fishers_count:
        ship_price -= ship_price * 0.25
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
    if fishers_count <= 6:
        ship_price -= ship_price * 0.1
    elif 7 <= fishers_count <= 11:
        ship_price -= ship_price * 0.15
    elif 12 <= fishers_count:
        ship_price -= ship_price * 0.25
elif season == "Winter":
    ship_price = 2600
    if fishers_count <= 6:
        ship_price -= ship_price * 0.1
    elif 7 <= fishers_count <= 11:
        ship_price -= ship_price * 0.15
    elif 12 <= fishers_count:
        ship_price -= ship_price * 0.25

if fishers_count % 2 == 0 and season == "Summer":
    ship_price -= ship_price * 0.05
if fishers_count % 2 == 0 and season == "Spring":
    ship_price -= ship_price * 0.05
if fishers_count % 2 == 0 and season == "Winter":
    ship_price -= ship_price * 0.05

if budged >= ship_price:
    print(f"Yes! You have {budged - ship_price:.2f} leva left.")
elif budged < ship_price:
    print(f"Not enough money! You need {ship_price - budged:.2f} leva.")
