from collections import defaultdict
from itertools import combinations, pairwise

with open("input.txt") as file:
    edges = [row.split("-") for row in file.read().splitlines()]

adj = defaultdict(set)

for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)

components = set()

for u in adj:
    for v, w in combinations(adj[u], r=2):
        nodes = (u, v, w)
        if v in adj[w] and any(n.startswith("t") for n in nodes):
            components.add(tuple(sorted(nodes)))

print(len(components))


def bron_kerbosch(r, p, x):
    if not p and not x:
        cliques.append(r)

    for v in list(p):
        neighbours = adj[v]
        bron_kerbosch(r | {v}, p & neighbours, x & neighbours)
        p.remove(v)
        x.add(v)


cliques = []
bron_kerbosch(set(), set(adj), set())

print(",".join(sorted(max(cliques, key=len))))
