import numpy as np

with open("input.txt") as file:
    forest = np.array(list(map(list, file.read().splitlines()))).astype(np.ushort)


def solution_1():
    trees_visible = 0

    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tree = forest[y][x]
            sides_visible = 4

            for d in range(y + 1, len(forest)):
                if tree <= forest[d][x]:
                    sides_visible -= 1
                    break

            for u in range(y - 1, -1, -1):
                if tree <= forest[u][x]:
                    sides_visible -= 1
                    break

            for r in range(x + 1, len(forest[y])):
                if tree <= forest[y][r]:
                    sides_visible -= 1
                    break

            for l in range(x - 1, -1, -1):
                if tree <= forest[y][l]:
                    sides_visible -= 1
                    break

            if sides_visible > 0:
                trees_visible += 1

    print(trees_visible)


def solution_1_v2():
    global forest
    forest = np.array(forest)

    trees_visible = 0
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tree = forest[y][x]

            down = forest[(y + 1):len(forest), x]
            up = forest[:y, x]
            right = forest[y, (x + 1):len(forest)]
            left = forest[y, :x]

            if len(down) == 0 or len(up) == 0 or len(right) == 0 or len(left) == 0:
                trees_visible += 1

            elif tree > max(down) or tree > max(up) or tree > max(right) or tree > max(left):
                trees_visible += 1

    print(trees_visible)


def solution_2():
    scenic_scores = []
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tree = forest[y][x]

            down = 0
            for d in range(y + 1, len(forest)):
                down += 1
                if tree <= forest[d][x]:
                    break

            up = 0
            for u in range(y - 1, -1, -1):
                up += 1
                if tree <= forest[u][x]:
                    break

            right = 0
            for r in range(x + 1, len(forest[y])):
                right += 1
                if tree <= forest[y][r]:
                    break

            left = 0
            for l in range(x - 1, -1, -1):
                left += 1
                if tree <= forest[y][l]:
                    break

            scenic_scores.append(down * up * left * right)

    print(max(scenic_scores))


def solution_2_v2():
    print(max(
        np.prod([len(score) if score.all() else np.argmax(~score) + 1 for score in [
            np.asarray(forest[(y + 1):, x] < forest[y, x]),
            np.asarray(forest[:y, x][::-1] < forest[y, x]),
            np.asarray(forest[y, (x + 1):] < forest[y, x]),
            np.asarray(forest[y, :x][::-1] < forest[y, x])
        ]]) for y in range(1, len(forest) - 1) for x in range(1, len(forest[y]) - 1)
    ))


solution_2_v2()
