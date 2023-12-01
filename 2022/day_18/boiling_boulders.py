import numpy as np

with open("input.txt", "r") as file:
    cubes = [tuple(map(int, row.split(","))) for row in file]

OFFSETS = [
    (+1, 0, 0),
    (-1, 0, 0),
    (0, +1, 0),
    (0, -1, 0),
    (0, 0, +1),
    (0, 0, -1)
]


def part_1():
    return sum([1 for x, y, z in cubes for dx, dy, dz in OFFSETS if (x + dx, y + dy, z + dz) not in cubes])


def part_2():
    mins = [min(np.array(cubes)[:, i] - 1) for i in range(3)]
    maxs = [max(np.array(cubes)[:, i] + 1) for i in range(3)]

    lava = np.zeros([mx + 1 for mx in maxs])

    for cube in cubes:
        lava[cube] = 1

    surface_area = set()
    visited = set()
    queue = [(0, 0, 0)]

    while queue:
        pos = queue.pop()
        visited.add(pos)

        for offset in OFFSETS:
            new_pos = tuple(n + dn for n, dn in zip(pos, offset))

            if new_pos in visited:
                continue

            if any(p < mn or p > mx for p, mn, mx in zip(new_pos, mins, maxs)):
                continue

            if lava[new_pos] == 1:
                surface_area.add((pos, new_pos))

            else:
                queue.append(new_pos)

    return len(surface_area)


print(part_1())
print(part_2())
