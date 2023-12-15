from math import prod, ceil

with open("input.txt") as file:
    times, distances = file.readlines()

t1 = list(map(int, times.strip("Time: ").split()))
d1 = list(map(int, distances.strip("Distance: ").split()))

print(prod(sum(i * (t - i) > d for i in range(t + 1)) for t, d in zip(t1, d1)))

t2 = int(times.strip("Time:").replace(" ", ""))
d2 = int(distances.strip("Distance:").replace(" ", ""))

# O(1)
det = (t2 ** 2 - d2 * 4) ** 0.5
x1, x2 = (t2 + det) / 2, (t2 - det) / 2
print(ceil(x1) - ceil(x2) + int(x1.is_integer() and x2.is_integer()))

# O(n)
print(sum(i * (t2 - i) > d2 for i in range(t2 + 1)))
