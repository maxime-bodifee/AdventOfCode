import re
from functools import cache


@cache
def arrangements(symbols, nums, current=0):
    if not symbols:
        return not nums and current == 0

    results = 0
    p = "#." if symbols[0] == "?" else symbols[0]
    for c in p:
        if c == "#":
            results += arrangements(symbols[1:], nums, current + 1)
        else:
            if current > 0:
                if nums and nums[0] == current:
                    results += arrangements(symbols[1:], nums[1:])
            else:
                results += arrangements(symbols[1:], nums)
    return results


def part_1(springs):
    return sum(arrangements(sy + ".", nu) for sy, nu in springs)


def part_2(springs):
    return sum(arrangements("?".join([sy] * 5) + ".", nu * 5) for sy, nu in springs)


if __name__ == '__main__':
    with open("input.txt") as file:
        inp = [[re.sub(r"\.+", ".", a), tuple(map(int, b.split(",")))]
               for line in file.read().splitlines() for a, b in [line.split()]]

    print(part_1(inp))
    print(part_2(inp))
