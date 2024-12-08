from collections import defaultdict
from itertools import combinations

with open("input.txt") as file:
    grid = {(x, y): char for y, row in enumerate(file.read().splitlines()) for x, char in enumerate(row)}

freqs = defaultdict(list)

for pos, char in grid.items():
    if char != ".":
        freqs[char].append(pos)


antinodes_1 = set()

for freq, antennas in freqs.items():
    for (xa, ya), (xb, yb) in combinations(antennas, 2):
        dx, dy = xa - xb, ya - yb

        if (xa + dx, ya + dy) in grid:
            antinodes_1.add((xa + dx, ya + dy))

        if (xb - dx, yb - dy) in grid:
            antinodes_1.add((xb - dx, yb - dy))

print(len(antinodes_1))


antinodes_2 = set()

for freq, antennas in freqs.items():
    for pos in antennas:
        antinodes_2.add(pos)

    for (xa, ya), (xb, yb) in combinations(antennas, 2):
        dx, dy = xa - xb, ya - yb

        nx, ny = xa + dx, ya + dy
        while (nx, ny) in grid:
            antinodes_2.add((nx, ny))
            nx, ny = nx + dx, ny + dy

        nx, ny = xb - dx, yb - dy
        while (nx, ny) in grid:
            antinodes_2.add((nx, ny))
            nx, ny = nx - dx, ny - dy

print(len(antinodes_2))

