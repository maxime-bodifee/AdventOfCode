

def traverse(instructions):
    dirs = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    x, y, p, v = 0, 0, 0, [(0, 0)]
    for d, s in instructions:
        dx, dy = dirs[d]
        x, y, p = x + s * dx, y + s * dy, p + s
        v.append((x, y))

    return area(p, v)


def area(p, v):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    a = sum(v[i][0] * v[i + 1][1] - v[i + 1][0] * v[i][1] for i in range(len(v) - 1))
    a += v[-1][0] * v[0][1] - v[0][0] * v[-1][1]

    # https://en.wikipedia.org/wiki/Pick's_theorem
    return p + (a - p) // 2 + 1


def part_1(steps):
    return traverse([(d, int(s)) for d, s, _ in steps])


def part_2(steps):
    return traverse([(["R", "D", "L", "U"][int(c[-2])], int(c[2:-2], 16)) for *_, c in steps])


if __name__ == '__main__':
    with open("input.txt") as file:
        inp = list(map(str.split, file.read().splitlines()))

    print(part_1(inp))
    print(part_2(inp))
