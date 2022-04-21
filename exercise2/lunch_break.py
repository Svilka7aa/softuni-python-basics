from math import ceil

series_name = input()
episode_duration = int(input())
brake_duration = int(input())

lunch_time = brake_duration * 1 / 8
brake_time = brake_duration * 1 / 4
time_left = brake_duration - lunch_time - brake_time

if time_left >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left - episode_duration)}"
          f" minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_duration - time_left)}"
          f" more minutes.")