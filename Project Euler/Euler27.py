import math

# getting list of primes < 1000
b_range = 1001
b_possibilities = [number for number in range(2, 1001)]
for i in range(2, math.ceil(math.sqrt(b_range))):
    if b_possibilities[i] == "False":
        pass
    else:
        multiple = 2 * i
        while multiple < b_range:
            multiple_index = multiple - 2
            # noinspection PyTypeChecker
            b_possibilities[multiple_index] = "False"
            multiple += i
primes_b = [number for number in b_possibilities if number != "False"]
primes_a = []
for primes in primes_b:
    primes_a.append(primes)
    primes_a.append(-primes)


# creating function to determine if prime or not
def is_prime(n):
    if n < 2:
        return False
    else:
        for numbers in range(2, math.floor(math.sqrt(n))+1):
            if n % numbers == 0:
                return False
        return True


b_coeff = []
a_coeff = []
# iterating over possible b's
for b in primes_b:
    # iterating over possible a's
    for a in primes_a:
        b_coeff.append(b)
        a_coeff.append(a)

consecutive_primes = []
# checking for # of consecutive primes
for index in range(len(b_coeff)):
    n = -1
    quadratic_number = 2
    a_value = a_coeff[index]
    b_value = b_coeff[index]
    while is_prime(quadratic_number):
        n += 1
        quadratic_number = n**2 + a_value * n + b_value
    consecutive_primes.append(n)

max_primes_index = consecutive_primes.index(max(consecutive_primes))
a_coefficient = a_coeff[max_primes_index]
b_coefficient = b_coeff[max_primes_index]
print("a: {0}, b: {1}, consecutive primes: {2}, product: {3}".format(a_coefficient, b_coefficient, max(consecutive_primes), a_coefficient*b_coefficient))
