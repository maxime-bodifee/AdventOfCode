import heapq
from collections import defaultdict

directions = {i: d for i, d in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)])}

with open("input.txt") as file:
    grid = list(map(list, file.read().splitlines()))
    start, end = (1, len(grid) - 2), (len(grid[0]) - 2, 1)
    grid = {(x, y): char for y, row in enumerate(grid) for x, char in enumerate(row)}


grid_score = defaultdict(lambda: (1e+10, -1))
best_path_tiles = set()

q = [[0, 0, start, set()]]
while q:
    score, direction, pos, visited = heapq.heappop(q)
    x, y = pos

    if (x, y) == end:
        best_path_tiles.update(visited)
        continue

    for new_direction, (dx, dy) in directions.items():
        new_pos = x + dx, y + dy
        if new_pos in visited or grid[new_pos] == "#":
            continue

        new_score = score + (1_001 if new_direction != direction else 1)

        old_score, old_direction = grid_score[new_pos]
        if new_score > old_score + (1_000 if new_direction != old_direction else 0):
            continue

        grid_score[new_pos] = new_score, new_direction
        heapq.heappush(q, [new_score, new_direction, new_pos, visited.union({pos})])

print(grid_score[end][0])
print(len(best_path_tiles.union({end})))
