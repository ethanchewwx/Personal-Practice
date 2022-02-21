factorial = 1
n = 100

for i in range(n, 0, -1):
    factorial *= i
print(factorial)

factorial_str = str(factorial)
total = 0
for j in range(len(factorial_str)):
    total += int(factorial_str[j])
print(total)
