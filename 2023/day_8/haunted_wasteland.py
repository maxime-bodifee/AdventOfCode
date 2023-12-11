from math import lcm


def steps(start):
    current = start
    i = 0
    while current[-1] != "Z":
        d = instructions[i % len(instructions)]
        current = nodes[current][d]
        i += 1

    return i


def part_1():
    return steps("AAA")


def part_2():
    return lcm(*(steps(node) for node in nodes if node[-1] == "A"))


if __name__ == "__main__":
    with open("input.txt") as file:
        instructions, _, *nodes = file.read().splitlines()

    instructions = list(map(int, list(instructions.replace("L", "0").replace("R", "1"))))
    nodes = [node.replace("= (", "").replace(",", "").replace(")", "").split() for node in nodes]
    nodes = {s: (l, r) for s, l, r in nodes}

    print(part_1())
    print(part_2())
