all_chains = []

for n in range(2, 1000000):
    chain = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            chain += 1
        else:
            n = (3 * n + 1) // 2
            chain += 2
    all_chains.append(chain)

print(all_chains.index(max(all_chains)))
