def sum_of_squares(number):
    total = 0
    for i in range(number + 1):
        total += i ** 2
    return total


def square_of_sum(number):
    total = 0
    for i in range(number + 1):
        total += i
    squared_total = total ** 2
    return squared_total


def difference(a, b):
    answer = b - a
    print(answer)


c = sum_of_squares(100)
d = square_of_sum(100)
difference(c, d)
