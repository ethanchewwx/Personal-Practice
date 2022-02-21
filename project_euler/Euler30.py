iteration_end = 354294
iteration_start = 64
power = 5
viable_numbers = []
total_sum = 0


def is_sum_of_digits(num):
    number_str = str(num)
    list_of_digits = [digit for digit in number_str]
    total = 0
    for digits in list_of_digits:
        total += int(digits)**power
    if total == num:
        return True
    else:
        return False


for number in range(iteration_start, iteration_end + 1):
    if is_sum_of_digits(number):
        viable_numbers.append(number)
        total_sum += number

print(viable_numbers)
print(total_sum)
