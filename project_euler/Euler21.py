def d(n):
    total = 1
    root_n = n ** (1/2)
    for i in range(2, root_n.__floor__() + 1):
        if i ** 2 == n:
            total += i
        elif n % i == 0:
            total += i + n//i
    return total


amicable_sum = 0
factors_all_numbers = {2: 1}
for number in range(3, 10000):
    sum_divisors = d(number)
    if sum_divisors in factors_all_numbers.keys() and number != sum_divisors:
        if factors_all_numbers[sum_divisors] == number:
            amicable_sum += number + sum_divisors
    factors_all_numbers[number] = sum_divisors

print(amicable_sum)
