record_in_seconds = float(input())
distance_in_metres = float(input())
time_per_meter = float(input())

distance_to_Swin_in_Seconds = distance_in_metres * time_per_meter
time_delays = (distance_in_metres // 15) * 12.5
time_sum = distance_to_Swin_in_Seconds + time_delays

if record_in_seconds <= time_sum:
    print(f"No, he failed! He was {abs(time_sum - record_in_seconds):.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {time_sum:.2f} seconds.")