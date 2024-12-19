
from itertools import pairwise

with open("input.txt") as file:
    grid = {(x, y): char for y, row in enumerate(file.read().splitlines()) for x, char in enumerate(row)}

regions = []

visited = set()
for pos, char in grid.items():
    if pos in visited:
        continue

    region = set()
    q = [pos]
    while q:
        pos = q.pop(0)
        if pos in visited:
            continue

        visited.add(pos)
        region.add(pos)

        x, y = pos
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_pos = (x + dx, y + dy)
            if grid.get(new_pos, "") == char:
                q.append(new_pos)

    regions.append(region)


total_1 = 0

for region in regions:
    perimeter = 0
    for x, y in region:
        perimeter += 4 - sum((x + dx, y + dy) in region for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)])

    total_1 += len(region) * perimeter

print(total_1)

# alternative calculation of total_1 lol
print(sum(
    len(region) * sum(
        4 - sum(
            (x + dx, y + dy) in region
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ) for x, y in region
    ) for region in regions
))


total_2 = 0

for region in regions:
    corners = 0
    for x, y in region:
        for (dx1, dy1), (dx2, dy2) in pairwise([(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0)]):
            neighbour_left, neighbour_right, neighbour_diagonal = (x + dx1, y + dy1), (x + dx2, y + dy2), (x + dx1 + dx2, y + dy1 + dy2)

            # outer corner
            if (neighbour_left not in region) and (neighbour_right not in region):
                corners += 1

            # inner corner
            if (neighbour_left in region) and (neighbour_right in region) and (neighbour_diagonal not in region):
                corners += 1

    total_2 += len(region) * corners


print(total_2)
