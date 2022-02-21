number_of_factors = 0
i = 0
triangle_number = 0

while number_of_factors < 500:
    list_of_factors = []
    i += 1
    triangle_number += i
    # obtain list of numbers from 1 up to ceiling of sqrt of triangle number
    ceiling = (triangle_number ** (1/2)).__ceil__()
    for number in range(1, ceiling):
        list_of_factors.append(number)
    end = len(list_of_factors)
    # iterating across the list of numbers to see whether it's a factor
    for factor_index in range(end):
        # if not factor then go through each of its multiple and put it as false
        if list_of_factors[factor_index] and triangle_number % list_of_factors[factor_index] != 0:
            for not_factor_index in range(factor_index, end, list_of_factors[factor_index]):
                list_of_factors[not_factor_index] = False
    if triangle_number == 1:
        number_of_factors = 1
    elif ceiling ** 2 == triangle_number:
        number_of_factors = (2 * (end - list_of_factors.count(False)) - 1)
    else:
        number_of_factors = 2 * (end - list_of_factors.count(False))

print(triangle_number, " number of factors = {}".format(number_of_factors))
# print(testing_list)
# print(list_of_factors.count(False))
