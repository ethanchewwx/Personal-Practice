i = 0
end = 114320
list_of_numbers = []

for k in range(2, end + 1):
    list_of_numbers.append(k)

while i < 10002:
    j = 2
    prime = list_of_numbers[i]
    while prime * j < (end + 1):
        if prime * j  in list_of_numbers:
            list_of_numbers.remove(prime * j)
        j += 1
    i += 1

print(list_of_numbers[10001])


# def is_prime(x):
#     for i in range(2, x // 2 + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
# j = 1
# k = 2
# while True:
#     if is_prime(k):
#         if j == 10001:
#             print(k)
#             break
#         k += 1
