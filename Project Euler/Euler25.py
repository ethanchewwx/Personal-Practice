f_1 = 0
f_2 = 1
fibonacci_next = 0
fibonacci_seq = [1]

i = 0
while len(str(fibonacci_next)) < 1000:
    fibonacci_next = f_1 + f_2
    fibonacci_seq.append(fibonacci_next)
    i += 1
    f_1 = f_2
    f_2 = fibonacci_next
thousandth_index = i + 1
print(thousandth_index)
