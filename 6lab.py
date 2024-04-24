def permutations(items):
    if len(items) <= 1:
        yield items
    else:
        for perm in permutations(items[1:]):
            for i in range(len(items)):
                yield perm[:i] + items[0:1] + perm[i:]


my_list = [1, 5, 9]
for permutation in permutations(my_list):
    print(permutation)

for permutation in permutations(my_list):
    print(permutation)
