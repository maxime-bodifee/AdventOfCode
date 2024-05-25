# reference: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21


def walk(grid):
    sy, sx = [(i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char == "S"][0]
    v, q = {(sx, sy): 0}, [(sx, sy)]

    while q:
        x, y = q.pop(0)
        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if grid[ny][nx] == "." and (nx, ny) not in v:
                    v[(nx, ny)] = v[(x, y)] + 1
                    q.append((nx, ny))

    return v.values()


def part_1(dists):
    return sum(1 for dist in dists if dist % 2 == 0 and dist <= 64)


def part_2(dists, n):
    even_corners = sum(1 for dist in dists if dist % 2 == 0 and dist > 65)
    odd_corners = sum(1 for dist in dists if dist % 2 == 1 and dist > 65)

    even_full = sum(1 for dist in dists if dist % 2 == 0)
    odd_full = sum(1 for dist in dists if dist % 2 == 1)

    return ((n + 1) ** 2) * odd_full + (n ** 2) * even_full - (n + 1) * odd_corners + n * even_corners


def main():
    with open("input.txt") as file:
        inp = file.read().splitlines()
    d = walk(inp)

    print(part_1(d))

    tiles = (26501365 - len(inp) // 2) // len(inp)
    print(part_2(d, tiles))


if __name__ == '__main__':
    main()
