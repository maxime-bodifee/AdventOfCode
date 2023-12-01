with open("input.txt") as file:
    input_txt = [[[int(num) for num in pair.split(",")] for pair in row.strip().split(" -> ")] for row in file]

X = 0
Y = 1

MAX_X = max([max([pair[0] for pair in row]) for row in input_txt])
MAX_Y = max([max([pair[1] for pair in row]) for row in input_txt])


def create_cave(input_txt):
    cave = [["." for _ in range((MAX_X + 1) + MAX_Y)] for _ in range(MAX_Y + 1)]

    for path in input_txt:
        for i in range(len(path) - 1):
            path_1 = path[i]
            path_2 = path[i + 1]

            if path_1[X] == path_2[X]:
                if path_2[Y] - path_1[Y] > 0:
                    for j in range(path_1[Y], path_2[Y] + 1):
                        cave[j][path_1[X]] = "#"

                else:
                    for j in range(path_2[Y], path_1[Y] + 1):
                        cave[j][path_1[X]] = "#"

            else:
                if path_2[X] - path_1[X] > 0:
                    for j in range(path_1[X], path_2[X] + 1):
                        cave[path_1[Y]][j] = "#"

                else:
                    for j in range(path_2[X], path_1[X] + 1):
                        cave[path_1[Y]][j] = "#"

    return cave


def fill_with_sand(cave, part):
    floor = False

    while not floor:
        sand = [500, 0]
        resting = False

        while not resting:
            if part == 1 and sand[Y] >= len(cave) - 1:
                floor = True
                break

            elif cave[sand[Y] + 1][sand[X]] not in ["#", "o"]:
                sand[Y] += 1

            elif cave[sand[Y] + 1][sand[X] - 1] not in ["#", "o"]:
                sand[Y] += 1
                sand[X] -= 1

            elif cave[sand[Y] + 1][sand[X] + 1] not in ["#", "o"]:
                sand[Y] += 1
                sand[X] += 1

            elif part == 2 and sand == [500, 0]:
                cave[sand[Y]][sand[X]] = "o"
                floor = True
                break

            else:
                cave[sand[Y]][sand[X]] = "o"
                resting = True

    return cave


def solution_1():
    print(sum([len(list(filter(lambda c: c == "o", row))) for row in fill_with_sand(create_cave(input_txt), 1)]))


def solution_2():
    cave = create_cave(input_txt)

    cave.append(["." for _ in range((MAX_X + 1) + MAX_Y)])
    cave.append(["#" for _ in range((MAX_X + 1) + MAX_Y)])

    print(sum([len(list(filter(lambda c: c == "o", row))) for row in fill_with_sand(cave, 2)]))


solution_2()
