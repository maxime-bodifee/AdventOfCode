from math import prod

import networkx as nx

if __name__ == '__main__':
    with open("input.txt") as file:
        inp = file.read().splitlines()

    G = nx.Graph()
    G.add_edges_from([(u, v) for row in inp for u, V in [row.split(": ")] for v in V.split()])
    G.remove_edges_from(nx.minimum_edge_cut(G))
    print(prod(len(cc) for cc in nx.connected_components(G)))
