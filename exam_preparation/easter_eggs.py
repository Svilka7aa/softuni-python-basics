number_of_red_eggs = 0
number_of_orange_eggs = 0
number_of_blue_eggs = 0
number_of_green_eggs = 0
number_of_max_eggs_from_same_colour = 0
color = " "

number_of_eggs = int(input())

for eggs in range(number_of_eggs):
    current_egg_colour = input()
    if current_egg_colour == "red":
        number_of_red_eggs += 1
        if number_of_red_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = number_of_red_eggs
            color = "red"
    elif current_egg_colour == "orange":
        number_of_orange_eggs += 1
        if number_of_orange_eggs > number_of_max_eggs_from_same_colour:
            number_of_orange_eggs = number_of_orange_eggs
            color = "orange"
    elif current_egg_colour == "blue":
        number_of_blue_eggs += 1
        if number_of_blue_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = number_of_blue_eggs
            color = "blue"
    elif current_egg_colour == "green":
        number_of_green_eggs += 1
        if number_of_green_eggs > number_of_max_eggs_from_same_colour:
            number_of_max_eggs_from_same_colour = number_of_green_eggs
            color = "green"


print(f"Red eggs: {number_of_red_eggs}")
print(f"Orange eggs: {number_of_orange_eggs}")
print(f"Blue eggs: {number_of_blue_eggs}")
print(f"Green eggs: {number_of_green_eggs}")
print(f"Max eggs: {number_of_max_eggs_from_same_colour} -> {color}")

