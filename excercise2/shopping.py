budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_card_price_for_one = 250

video_cards_price = video_cards_count * video_card_price_for_one

price_for_processor = video_cards_price * 0.35
price_for_ram = video_cards_price * 0.10

processors_total = processors_count * price_for_processor
ram_total = ram_count * price_for_ram

price_total = video_cards_price + processors_total + ram_total

if video_cards_count > processors_count:
    price_total = price_total - (price_total * 0.15)

if price_total <= budget:
    print(f"You have {(budget - price_total):.2f} leva left!")
else:
    print(f"Not enough money! You need {(price_total - budget):.2f} leva more!")






