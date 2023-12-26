import heapq

V, H = 0, 1


def adjacency(min_step, max_step):
    max_x, max_y = len(inp[0]), len(inp)
    adj = [[[[], []] for _ in range(len(inp[0]))] for _ in range(len(inp))]
    for y, row in enumerate(inp):
        for x, char in enumerate(row):
            for i in range(-max_step, max_step + 1):
                if abs(i) < min_step:
                    continue
                j = i // abs(i)
                m, n = (i, j) if i < j else (j, i)
                if 0 <= x + i < max_x:
                    adj[y][x][H].append(((x + i, y), sum(inp[y][x + j] for j in range(m, n + 1))))
                if 0 <= y + i < max_y:
                    adj[y][x][V].append(((x, y + i), sum(inp[y + j][x] for j in range(m, n + 1))))

    return adj


def dijkstra(adj):
    d = [[[float("inf")] * 2 for _ in range(len(inp[0]))] for _ in range(len(inp))]
    d[0][0] = [0., 0.]
    q = [(0., (0, 0), H), (0., (0, 0), V)]
    while q:
        cd, (x, y), k = heapq.heappop(q)

        if cd > d[y][x][k]:
            continue

        for (nx, ny), cost in adj[y][x][nk := k ^ 1]:
            if d[y][x][k] + cost < d[ny][nx][nk]:
                d[ny][nx][nk] = d[y][x][k] + cost
                heapq.heappush(q, (d[ny][nx][nk], (nx, ny), nk))

    return int(min(d[len(inp) - 1][len(inp[0]) - 1]))


if __name__ == '__main__':
    with open("input.txt") as file:
        inp = [[int(char) for char in list(row)] for row in file.read().splitlines()]

    print(dijkstra(adjacency(1, 3)))
    print(dijkstra(adjacency(4, 10)))
