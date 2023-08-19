import re
import math

# FOR PART 2
# edges = {(top left corner, direction): (start, end, rotation, new direction)}
edges = {(1, -1j): (50, 150j, 1j, 1),  # orange
         (3j, -1): (150j, 50, -1j, 1j),
         (2, -1j): (100, 199j, 1, -1j),  # pink
         (3j, 1j): (199j, 100, 1, 1j),
         (1, -1): (50, 149j, -1, 1),  # blue
         (2j, -1): (100j, 50 + 49j, -1, 1),
         (2, 1): (149, 99 + 149j, -1, -1),  # purple
         (1 + 2j, 1): (99 + 100j, 149 + 49j, -1, -1),
         (1 + 1j, -1): (50 + 50j, 100j, -1j, 1j),  # red
         (2j, -1j): (100j, 50 + 50j, 1j, 1),
         (2, 1j): (100 + 49j, 99 + 50j, 1j, -1),  # yellow
         (1 + 1j, 1): (99 + 50j, 100 + 49j, -1j, -1j),
         (1 + 2j, 1j): (50 + 149j, 49 + 150j, 1j, -1),  # green
         (3j, 1): (49 + 150j, 50 + 149j, -1j, -1j)}


def walk(pos, dir, part=1):
    for p in path:
        if p == "L":
            dir *= -1j

        elif p == "R":
            dir *= 1j

        else:
            for _ in range(int(p)):
                if pos + dir in grid:
                    new_pos = pos + dir
                    new_dir = dir

                elif part == 1:
                    new_pos = pos
                    new_dir = dir

                    while new_pos - dir in grid:
                        new_pos -= dir

                else:
                    top_left = complex(pos.real // n, pos.imag // n)
                    start, end, rotation, new_dir = edges[(top_left, dir)]

                    new_pos = (pos - start) * rotation + end

                if grid[new_pos] == ".":
                    pos = new_pos
                    dir = new_dir

    return int(1000 * (pos.imag + 1) + 4 * (pos.real + 1) + [1, 1j, -1, -1j].index(dir))


with open("input.txt") as file:
    *grid, _, path = file
    n = math.gcd(len(grid), len(grid[0].strip("\n")))
    pos, dir = grid[0].index('.'), 1

path = re.findall(r"\d+|[RL]", path)
grid = {complex(x, y): char for y, row in enumerate(grid) for x, char in enumerate(row) if char in ".#"}

print(walk(pos, dir))
print(walk(pos, dir, part=2))
