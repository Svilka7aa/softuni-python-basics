chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15

number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegan_menu = int(input())

chicken_menus = number_chicken_menus * chicken_menu_price
fish_menus = number_fish_menus * fish_menu_price
vegan_menus = number_vegan_menu * vegan_menu_price

menus_price = chicken_menus + fish_menus + vegan_menus

desert = menus_price * (20 / 100)

delivery = 2.50

total_price = menus_price + desert + delivery

print(total_price)