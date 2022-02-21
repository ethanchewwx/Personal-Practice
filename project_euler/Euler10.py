def is_prime(end):
    list_of_numbers = []
    for i in range(2, end + 1):
        list_of_numbers.append(i)

    for numbers in range(2, end + 1):
        # iterate up until sqrt(end)
        if numbers * numbers > end:
            break
        # perform only if not already tagged
        elif list_of_numbers[numbers - 2]:
            # sieve - marking all multiples of primes
            for numbers_multiple in range(2 * numbers, end + 1, numbers):
                list_of_numbers[numbers_multiple - 2] = False
    return list_of_numbers


print(sum(is_prime(2000000)))
# print(sum(number for number in is_prime(2000000) if not False))
