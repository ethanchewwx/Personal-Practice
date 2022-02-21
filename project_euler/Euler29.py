a_power_b_list = []

for a in range(2, 101):
    for b in range(2, 101):
        a_power_b = a ** b
        if a_power_b not in a_power_b_list:
            a_power_b_list.append(a_power_b)

print(sorted(a_power_b_list))
print(len(a_power_b_list))
