name = input()
best_player = " "
best_player_score = 0

while name != "END":
    score = int(input())
    if score > best_player_score:
        best_player_score = score
        best_player = name
        if score >= 10:
            break
    name = input()


if score >= 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_player_score} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_player_score} goals.")


