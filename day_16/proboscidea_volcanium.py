import networkx as nx
from bitarray import bitarray
import time

with open("input.txt") as file:
    input_txt = [row.strip() for row in file.readlines()]

valves = nx.DiGraph()
non_zero_valves = nx.DiGraph()


def release_pressure(node: str, visited: bitarray, minutes: int, is_elephant: bool):
    max_pressure = 0

    visited[nodes.index(node)] = 1

    for edge in non_zero_valves.neighbors(node):
        if non_zero_valves[node][edge]["time"] >= minutes or visited[nodes.index(edge)] == 1:
            continue

        pressure = release_pressure(edge, visited.copy(), minutes - non_zero_valves[node][edge]["time"], is_elephant)

        if pressure > max_pressure:
            max_pressure = pressure

    if max_pressure == 0 and is_elephant:
        max_pressure = release_pressure("AA", visited, 27, False)

    return max_pressure + non_zero_valves.nodes[node]["rate"] * (minutes - 1)


def solution_1():
    return release_pressure("AA", visited, 31, False)


def solution_2():
    return release_pressure("AA", visited, 27, True)


for i in range(len(input_txt)):
    if "; tunnels lead to valves " in input_txt[i]:
        line = input_txt[i].split("; tunnels lead to valves ")

    else:
        line = input_txt[i].split("; tunnel leads to valve ")

    valve = line[0].split(" has flow rate=")
    name = valve[0].split()[1]
    rate = int(valve[1])
    leads_to = line[1].split(", ")

    valves.add_node(name, rate=rate)
    valves.add_weighted_edges_from([(name, other, 1) for other in leads_to], weight="time")

    if rate > 0 or name == "AA":
        non_zero_valves.add_node(name, rate=rate)

for i in non_zero_valves.nodes():
    for j in non_zero_valves.nodes():
        if i == j:
            continue

        non_zero_valves.add_edge(i, j, time=len(nx.shortest_path(valves, i, j)))

nodes = list(non_zero_valves.nodes())
visited = bitarray("0" * len(nodes))

start_time = time.time()
print(solution_2())
end_time = time.time()

print(format(end_time - start_time, "f"), "seconds")
