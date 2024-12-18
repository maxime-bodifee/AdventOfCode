import re
import heapq
from collections import defaultdict

# gx, gy = 6, 6
gx, gy = 70, 70

with open("input.txt") as file:
    positions = [(int(a), int(b)) for a, b in re.findall(r"(\d+),(\d+)", file.read())]


def simulate(num_bytes: int):
    grid = {(x, y): ("#" if (x, y) in positions[:num_bytes] else ".") for x in range(gx + 1) for y in range(gy + 1)}

    adj = defaultdict(list)
    for (x, y), char in grid.items():
        if char == "#":
            continue

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in grid:
                continue

            if grid[(nx, ny)] == ".":
                adj[(x, y)].append((nx, ny))

    d = {pos: float("inf") for pos in grid}
    d[(0, 0)] = 0
    q = [(0, (0, 0))]
    while q:
        cost, pos = heapq.heappop(q)

        if cost > d[pos]:
            continue

        for new_pos in adj[pos]:
            if d[pos] + 1 < d[new_pos]:
                d[new_pos] = d[pos] + 1
                heapq.heappush(q, (d[new_pos], new_pos))

    return d[(gx, gy)]


for i, (x, y) in enumerate(positions[2800:], start=2801):
    if simulate(num_bytes=i) == float("inf"):
        print(f"{x},{y}")
        break
