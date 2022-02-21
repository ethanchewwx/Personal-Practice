def is_abundant(n):
    total = 1
    root_n = n ** (1/2)
    for i in range(2, root_n.__floor__() + 1):
        if i ** 2 == n:
            total += i
        elif n % i == 0:
            total += i + n//i
    if total > n:
        return True
    else:
        return False


abundant_numbers = [i for i in range(3, 28123) if is_abundant(i)]
all_numbers = [i for i in range(28123)]
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        if abundant_numbers[i] + abundant_numbers[j] < 28123:
            all_numbers[abundant_numbers[i] + abundant_numbers[j]] = 0
        else:
            break
print(sum(all_numbers))
print(abundant_numbers)
