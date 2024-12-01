from collections import Counter

with open("input.txt") as file:
    inp = file.read().splitlines()

inp = [list(map(int, row.split("   "))) for row in inp]
inp = [*zip(*inp)]
sorted_pairs = [*zip(sorted(inp[0]), sorted(inp[1]))]
print(sum(abs(a - b) for a, b in sorted_pairs))

counts = Counter(inp[1])
print(sum(a * counts.get(a, 0) for a in inp[0]))
