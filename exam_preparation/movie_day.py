time = int(input())
number_of_scenes = int(input())
time_per_scenes = int(input())
preparation_time = time * 0.15
total_time = number_of_scenes * time_per_scenes + preparation_time
difference = round(abs(total_time - time))

if time >= total_time:
    print(f"You managed to finish the movie on time! You have {difference} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {difference} minutes.")
