destination = input()
dates = input()
nights = int(input())
price_per_night = 0


if destination == "France":
    if dates == "21-23":
        price_per_night = 30
    elif dates == "24-27":
        price_per_night = 35
    elif dates == "28-31":
        price_per_night = 40
elif destination == "Italy":
    if dates == "21-23":
        price_per_night = 28
    elif dates == "24-27":
        price_per_night = 32
    elif dates == "28-31":
        price_per_night = 39
else:
    if dates == "21-23":
        price_per_night = 32
    elif dates == "24-27":
        price_per_night = 37
    elif dates == "28-31":
        price_per_night = 43


print(f"Easter trip to {destination} : {nights * price_per_night:.2f} leva.")
