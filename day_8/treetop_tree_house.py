with open("input.txt") as file:
    forest = file.readlines()
    forest = [[int(num) for num in row.strip()] for row in forest]


def solution_1():
    trees_visible = 0

    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tree = forest[y][x]

            down = True
            for d in range(y + 1, len(forest)):
                if tree > forest[d][x]:
                    continue
                else:
                    down = False
                    break

            up = True
            for u in range(y - 1, -1, -1):
                if tree > forest[u][x]:
                    continue
                else:
                    up = False
                    break

            right = True
            for r in range(x + 1, len(forest[y])):
                if tree > forest[y][r]:
                    continue
                else:
                    right = False
                    break

            left = True
            for l in range(x - 1, -1, -1):
                if tree > forest[y][l]:
                    continue
                else:
                    left = False
                    break

            if down or up or right or left:
                trees_visible += 1

    print(trees_visible)


def solution_2():
    scenic_scores = []
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tree = forest[y][x]

            down = 0
            for d in range(y + 1, len(forest)):
                if tree > forest[d][x]:
                    down += 1
                    continue
                else:
                    down += 1
                    break

            up = 0
            for u in range(y - 1, -1, -1):
                if tree > forest[u][x]:
                    up += 1
                    continue
                else:
                    up += 1
                    break

            right = 0
            for r in range(x + 1, len(forest[y])):
                if tree > forest[y][r]:
                    right += 1
                    continue
                else:
                    right += 1
                    break

            left = 0
            for l in range(x - 1, -1, -1):
                if tree > forest[y][l]:
                    left += 1
                    continue
                else:
                    left += 1
                    break

            scenic_scores.append(down*up*left*right)

    print(max(scenic_scores))


solution_2()
