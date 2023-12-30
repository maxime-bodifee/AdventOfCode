import time

X, Y, Z = 0, 1, 2


def fall(grid, bricks, i=0):
    fallen = 0
    for j, brick in enumerate(bricks, i):
        k = 0
        while all(z - k > 1 and grid[z - k - 1][y][x] in [-1, j, i - 1] for x, y, z in brick):
            k += 1

        if k > 0:
            for x, y, z in brick:
                grid[z][y][x] = -1
                grid[z - k][y][x] = j
            for cube in bricks[j - i]:
                cube[Z] -= k

            fallen += 1

    return fallen


def create_grid(inp):
    bricks = sorted([
        [[x1 + dx, y1 + dy, z1 + dz]
         for dx in range(x2 - x1 + 1) for dy in range(y2 - y1 + 1) for dz in range(z2 - z1 + 1)
         ] for line in inp for x1, y1, z1, x2, y2, z2 in [list(map(int, line.replace("~", ",").split(",")))]
    ], key=lambda n: max(c[Z] for c in n))

    cubes = [*zip(*[cube for brick in bricks for cube in brick])]
    max_x, max_y, max_z = max(cubes[X]), max(cubes[Y]), max(cubes[Z])

    grid = [[[-1] * (max_x + 1) for _ in range(max_y + 1)] for _ in range(max_z + 1)]
    for i, brick in enumerate(bricks):
        for x, y, z in brick:
            grid[z][y][x] = i

    fall(grid, bricks)
    return grid, bricks


def part_1(grid, bricks):
    return sum(
        not any(all(z > 1 and grid[z - 1][y][x] in [-1, j, i] for x, y, z in brick)
                for j, brick in enumerate(bricks[i + 1:], i + 1))
        for i in range(len(bricks))
    )


def part_2(grid, bricks):
    return sum(
        fall([[col[:] for col in row] for row in grid],
             [[cube[:] for cube in brick] for brick in bricks[i + 1:]],
             i + 1)
        for i in range(len(bricks))
    )


if __name__ == '__main__':
    with open("input.txt") as file:
        grid, bricks = create_grid(file.read().splitlines())

    t = time.perf_counter()
    print(f"part 1: {part_1(grid, bricks)}, time: {time.perf_counter() - t:.6f} seconds")

    t = time.perf_counter()
    print(f"part 2: {part_2(grid, bricks)}, time: {time.perf_counter() - t:.6f} seconds")
