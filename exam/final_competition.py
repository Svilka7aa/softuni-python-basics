dancers_count = int(input())
points = float(input())
season = input()
place = input()

prize = 0

if place == "Bulgaria":
    prize = dancers_count * points
elif place == "Abroad":
    prize = dancers_count * points + (dancers_count * points * 0.5)

if place == "Bulgaria":
    if season == "summer":
        costs = prize * 0.05
    elif season == "winter":
        costs = prize * 0.08

elif place == "Abroad":
    if season == "summer":
        costs = prize * 0.1
    elif season == "winter":
        costs = prize * 0.15

total = prize - costs
donation = total * 0.75
rest = total - donation
wins_per_person = rest /dancers_count

print(f"Charity - {donation:.2f}")
print(f"Money per dancer - {wins_per_person:.2f}")