from itertools import permutations

my_list = [1,2,3,4,5]

permutation_list = permutations(my_list)

for permutation in permutation_list:
    print(permutation)