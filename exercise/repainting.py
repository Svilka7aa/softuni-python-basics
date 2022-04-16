nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
working_hours = int(input())

nylon_sum_price = (nylon_quantity + 2) * nylon_price
paint_sum_price = (paint_quantity + (paint_quantity *10 / 100)) * paint_price
paint_thinner_sum_price = paint_thinner_quantity * paint_thinner_price

supplies_price_sum = nylon_sum_price + paint_sum_price + paint_thinner_sum_price + 0.40

workers_price = (supplies_price_sum * ( 30 / 100)) * working_hours

total = supplies_price_sum + workers_price


print(total)
