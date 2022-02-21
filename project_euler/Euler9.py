final_sum = 1000
pythagorean_triplet = []

for a in range(1, final_sum):
    for b in range(a + 1, final_sum - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            product = a * b * c
            print("a: {0}, b: {1}, c: {2}  product = {3}".format(a, b, c, product))
            break

# squared_numbers = []

# for i in range(1, (final_sum**(1/2)).__floor__() + 1):
#     squared_numbers.append(i ** 2)
# print(squared_numbers)

# for i in range(1, final_sum + 1):
#     squared_numbers.append(i ** 2)

# length_squared_numbers = len(squared_numbers)

# for j in range(length_squared_numbers):
#     for k in (range(j + 1, length_squared_numbers)):
#         c_squared = squared_numbers[j] + squared_numbers[k]
#         if c_squared in squared_numbers:
#             candidate = [squared_numbers[j], squared_numbers[k], c_squared]
#             pythagorean_triplet.append(candidate)
# print(pythagorean_triplet)
