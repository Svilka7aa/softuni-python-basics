import math

days = int(input())
kilometers_first_day = float(input())
target = 1000
kilometers_today = 0
kilometers_total = 0

if kilometers_total < kilometers_first_day:
    kilometers_total = kilometers_first_day


for kilometers in range(days):
    percent = int(input())
    if kilometers_first_day > kilometers_today:
        kilometers_today = kilometers_first_day

    kilometers_today += kilometers_today * percent / 100
    kilometers_total += kilometers_today

if kilometers_total >= target:
    print(f"You've done a great job running {math.ceil(kilometers_total - target)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(target - kilometers_total)} more kilometers")
