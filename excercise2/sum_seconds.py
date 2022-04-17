time_first = int(input())
time_second = int(input())
time_third = int(input())

time_sumed = time_first + time_second + time_third

minutes = time_sumed // 60
seconds = time_sumed % 60

if seconds <= 9:
    print(f'{minutes}:0{seconds}')

else:
    print(f"{minutes}:{seconds}")
