def get_recurring(den):
    num = 1
    remainder = num
    current_index = 0
    quotient_list = []
    remainder_list = []
    while remainder != 0:
        remainder *= 10
        quotient = remainder//den
        if remainder not in remainder_list:
            quotient_list.append(quotient)
            remainder_list.append(remainder)
            current_index += 1
        else:
            first_index = remainder_list.index(remainder)
            length_recurring = current_index - first_index
            return length_recurring
        remainder = remainder % den
    return 0


length_recurring_set = []
for i in range(1, 1000):
    length_recurring_set.append(get_recurring(i))
max_length = max(length_recurring_set)
print("denominator: {0}, recurring length: {1}".format(length_recurring_set.index(max_length) + 1, max_length))

