from math import prod


def part_1(txt):
    maximum = {"red": 12, "green": 13, "blue": 14}
    return sum(i if all(maximum[k] >= v for r in g for k, v in r.items()) else 0 for i, g in enumerate(txt, 1))


def part_2(txt):
    p = 0
    for game in txt:
        cubes = {"red": [], "green": [], "blue": []}
        [cubes[k].append(v) for r in game for k, v in r.items()]
        p += prod(max(colour) for colour in cubes.values())

    return p


if __name__ == "__main__":
    with open("input.txt") as file:
        input_txt = [[game.split() for game in line[5:].split(";")] for line in file.readlines()]

    for i, game in enumerate(input_txt):
        input_txt[i][0] = game[0][1:]
        input_txt[i] = [{r[j + 1].strip(","): int(r[j]) for j in range(0, len(r), 2)} for r in game]

    print(part_1(input_txt))
    print(part_2(input_txt))
