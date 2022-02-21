start = 20
i = 11

while i < 21:
    if start % i == 0:
        i += 1
    else:
        start += 20
        i = 11

print(start)


# check_list = [11, 13, 14, 16, 17, 18, 19, 20]
# starting = 20
# j = 0
#
# while j < len(check_list)\
#         :
#     if starting % check_list[j] == 0:
#         j += 1
#     else:
#         starting += 20
#         j = 0
#
# print(starting)
