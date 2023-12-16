from functools import reduce


def h(s):
    return reduce(lambda v, c: (v + ord(c)) * 17 % 256, s, 0)


def part_1(steps):
    return sum(h(s) for s in steps)


def part_2(steps):
    bx = [{} for _ in range(256)]
    for s in steps:
        if s.endswith("-"):
            bx[h(s[:-1])].pop(s[:-1], None)

        else:
            l, fl = s.split("=")
            bx[h(l)][l] = int(fl)

    return sum(bi * s * fl for bi, b in enumerate(bx, 1) for s, fl in enumerate(b.values(), 1))


def main():
    with open("input.txt") as file:
        inp = file.read().split(",")

    print(part_1(inp))
    print(part_2(inp))


if __name__ == '__main__':
    main()
