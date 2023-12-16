m = {
    ("/", 1j): -1, ("/", 1): -1j, ("/", -1): 1j, ("/", -1j): 1,
    ("\\", 1j): 1, ("\\", -1): -1j, ("\\", 1): 1j, ("\\", -1j): -1
}


def energized(p):
    q, v = [p], set()
    while q:
        pos, d = q.pop()
        while (pos, d) not in v and 0 <= pos.real < len(grid[0]) and 0 <= pos.imag < len(grid):
            v.add((pos, d))
            x, y = int(pos.real), int(pos.imag)
            if (c := grid[y][x]) in "/\\":
                d = m[(c, d)]

            elif c == "-" and d in [1j, -1j]:
                q.append((pos, 1))
                d = -1

            elif c == "|" and d in [1, -1]:
                q.append((pos, 1j))
                d = -1j

            pos += d

    return len({c for c, _ in v})


def part_1():
    return energized((0, 1))


def part_2():
    b = [((i * 1j, 1), (len(grid[0]) - 1 + i * 1j, -1)) for i in range(len(grid))] + \
        [((i, 1j), (i + (len(grid) - 1) * 1j, -1j)) for i in range(1, len(grid[0]) - 1)]
    return max(energized(p) for ps in b for p in ps)


if __name__ == "__main__":
    with open("input.txt") as file:
        grid = list(map(list, file.read().splitlines()))

    print(part_1())
    print(part_2())
