n = int(input())
for a in range(1, 9 + 1):
    for b in range(9, a + 1):
        for c in range(9 + 1):
            for d in range(9, c + 1):

                if (a + b + c + d) == (a * b * c * d) and n % 5 == 0:
                    print(f"{a,b,c,d}")
                elif (a * b * c * d) / (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d,c,b,a}")
                    break
                else:
                    print("Nothing found")

