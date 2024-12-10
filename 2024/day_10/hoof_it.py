

def bfs(pos, num):
    trails = set()

    q = [(pos, num)]
    while q:
        pos, num = q.pop(0)

        if num == 9:
            trails.add(pos)
            continue

        x, y = pos
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            npos = x + dx, y + dy
            if grid.get(npos, -1) == num + 1:
                q.append((npos, num + 1))

    return len(trails)


def dfs(pos, num):
    if num == 9:
        return 1

    candidates = []

    x, y = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        npos = x + dx, y + dy
        if grid.get(npos, -1) == num + 1:
            candidates.append((npos, num + 1))

    if candidates:
        return sum(dfs(p, n) for p, n in candidates)

    return 0


with open("input.txt") as file:
    grid = {(x, y): int(num) for y, row in enumerate(file.read().splitlines()) for x, num in enumerate(row)}

print(sum(bfs(pos, num) for pos, num in grid.items() if num == 0))
print(sum(dfs(pos, num) for pos, num in grid.items() if num == 0))
