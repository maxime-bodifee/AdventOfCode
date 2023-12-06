from math import prod

with open("input.txt") as file:
    times, distances = file.readlines()

t1 = list(map(int, times.strip("Time: ").split()))
d1 = list(map(int, distances.strip("Distance: ").split()))

print(prod(sum(i * (t - i) > d for i in range(t + 1)) for t, d in zip(t1, d1)))

t2 = int(times.strip("Time:").replace(" ", ""))
d2 = int(distances.strip("Distance:").replace(" ", ""))

print(sum(i * (t2 - i) > d2 for i in range(t2 + 1)))
