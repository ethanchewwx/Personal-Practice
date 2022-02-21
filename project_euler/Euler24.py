from itertools import permutations
all_permutations_list = list(permutations(range(0, 10)))

millionth_permutation_set = all_permutations_list[999999]
millionth_permutation_set_str = [str(number) for number in millionth_permutation_set]
millionth_permutation = "".join(millionth_permutation_set_str)
print(millionth_permutation)

