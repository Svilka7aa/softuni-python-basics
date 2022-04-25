command = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != "stop":
    is_prime = True
    current_num = int(command)
    for number in range(2, current_num):
        if current_num % number == 0:
            is_prime = False
    if current_num < 0:
        print("Number is negative.")
        command = input()
        continue

    if is_prime:
        prime_numbers_sum += current_num
    else:
        non_prime_numbers_sum += current_num

    command = input()



print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")