rows_columns = 1001
total_squares = (rows_columns - 1)//2
total_sum = 1
start = 1

for square_number in range(1, total_squares + 1):
    for corners in range(4):
        start += 2 * square_number
        total_sum += start
print(total_sum)