groups_count = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_people = 0

for group in range(groups_count):
    people = int(input())

    if people <= 5:
        musala += people

    elif people <= 12:
        monblan += people

    elif people <= 25:
        kilimanjaro += people

    elif people <= 40:
        k2 += people

    else:
        everest += people

    all_people += people

musala = musala / all_people * 100
monblan = monblan / all_people * 100
kilimanjaro = kilimanjaro / all_people * 100
k2 = k2 / all_people * 100
everest = everest / all_people * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
