number = 2 ** 1000

total = 0
for digits in str(number):
    total += int(digits)

print(total)
