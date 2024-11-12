def radix_sort(lst, phase):
    pattern = list(range(len(lst[0])))
    bins = [[] for _ in range(26)]
    for i in range(phase):
        a = [lst[-i-1][j] for j in pattern]
        word = enumerate([ord(c) - 97 for c in a])
        for j, c in word:
            bins[c].append(j)
        new_pattern = [x for q in bins for x in q]
        pattern = [pattern[j] for j in new_pattern]
        bins = [[] for _ in range(26)]
    pattern = [x + 1 for x in pattern]
    return pattern


print(radix_sort(['bab', 'bba', 'baa'], 3))
