import time

with open("input.txt") as file:
    grid = [[char for char in row.strip()] for row in file]

OFFSETS = [
    (0, 0),
    (+1, 0),
    (-1, 0),
    (0, +1),
    (0, -1)
]


class Blizzard:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def move(self):
        match self.dir:
            case ">":
                self.x = 0 if grid[self.y][self.x + 1] == "#" else self.x
                self.x += 1

            case "<":
                self.x = len(grid[0]) - 1 if grid[self.y][self.x - 1] == "#" else self.x
                self.x -= 1

            case "v":
                self.y = 0 if grid[self.y + 1][self.x] == "#" else self.y
                self.y += 1

            case "^":
                self.y = len(grid) - 1 if grid[self.y - 1][self.x] == "#" else self.y
                self.y -= 1

        return self.x, self.y


def traverse(start, end, blizzards):
    mins = 0

    pos = {start}

    while end not in pos:
        new_pos = set()

        b_pos = set(b.move() for b in blizzards)

        for x, y in pos:
            for dx, dy in OFFSETS:
                nx, ny = x + dx, y + dy

                if ny < 0 or ny > len(grid) - 1:
                    continue

                if grid[ny][nx] == "#":
                    continue

                if (nx, ny) not in b_pos:
                    new_pos.add((nx, ny))

        pos = new_pos

        mins += 1

    return mins


def answer(part=1):
    blizzards = [Blizzard(j, i, char) for i, row in enumerate(grid) for j, char in enumerate(row)
                 if char in [">", "<", "v", "^"]]

    start = (1, 0)
    end = (len(grid[0]) - 2, len(grid) - 1)

    if part == 1:
        return traverse(start, end, blizzards)

    elif part == 2:
        return traverse(start, end, blizzards) + traverse(end, start, blizzards) + traverse(start, end, blizzards)


print(answer())
print(answer(part=2))
