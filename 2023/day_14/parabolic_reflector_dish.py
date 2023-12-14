

def tilt(grid, d):
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] == "O":
                if d == "up":
                    k = i
                    while k > 0 and grid[k - 1][j] not in "#O":
                        grid[k][j], grid[k - 1][j] = grid[k - 1][j], grid[k][j]
                        k -= 1
                elif d == "side":
                    k = j
                    while k > 0 and grid[i][k - 1] not in "#O":
                        grid[i][k], grid[i][k - 1] = grid[i][k - 1], grid[i][k]
                        k -= 1


def part_1(grid):
    tilt(grid, "up")
    return sum(i * row.count("O") for i, row in enumerate(grid[::-1], 1))


def part_2(grid):
    previous = []
    i = 0
    while True:
        tilt(grid, "up")
        tilt(grid, "side")
        grid = [row[::-1] for row in grid[::-1]]
        tilt(grid, "up")
        tilt(grid, "side")
        grid = [row[::-1] for row in grid[::-1]]

        if grid in previous:
            break

        previous.append([row.copy() for row in grid])
        i += 1

    j = previous.index(grid)
    k = (1_000_000_000 - j) % (i - j) + j - 1

    return sum(i * row.count("O") for i, row in enumerate(previous[k][::-1], 1))


if __name__ == "__main__":
    with open("input.txt") as file:
        inp = list(map(list, file.read().splitlines()))

    print(part_1(inp))
    print(part_2(inp))
