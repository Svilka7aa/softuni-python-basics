age = float(input())
gender = input()

# "Mr." – мъж (пол 'm') на 16 или повече години
# "Master" – момче (пол 'm') под 16 години
# "Ms." – жена (пол 'f') на 16 или повече години
# "Miss" – момиче (пол 'f') под 16 години

if gender == "m" and age >= 16:
    print("Mr.")
elif gender == "m" and age < 16:
    print("Master")
elif gender == "f" and age >= 16:
    print("Ms.")
else:
    print("Miss")