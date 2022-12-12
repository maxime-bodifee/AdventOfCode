with open("input.txt") as file:
    input_txt = file.readlines()


class Node:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col
        self.g_cost = 0
        self.h_cost = 0
        self.parent = None

    def f_cost(self):
        return self.g_cost + self.h_cost

    def set_h_cost(self, end: tuple):
        self.h_cost = abs((end[0] - self.row)) + abs((end[1] - self.col))

    def steps(self):
        if self.parent is None:
            return 0

        else:
            return self.parent.steps() + 1


def pathfinder(height_map: list[list[Node]], start, end):
    open_nodes: set[Node] = set()
    closed_nodes: set[Node] = set()

    open_nodes.add(height_map[start[0]][start[1]])

    while True:
        current_node: Node = min(open_nodes, key=lambda node: node.f_cost())

        open_nodes.remove(current_node)
        closed_nodes.add(current_node)

        if (current_node.row, current_node.col) == end:
            steps = current_node.steps()

            for row in height_map:
                for node in row:
                    node.parent = None

            return steps

        neighbours: list[Node] = []

        # down
        if current_node.row < len(height_map) - 1:
            neighbours.append(height_map[current_node.row + 1][current_node.col])

        # up
        if current_node.row > 0:
            neighbours.append(height_map[current_node.row - 1][current_node.col])

        # right
        if current_node.col < len(height_map[0]) - 1:
            neighbours.append(height_map[current_node.row][current_node.col + 1])

        # left
        if current_node.col > 0:
            neighbours.append(height_map[current_node.row][current_node.col - 1])

        for neighbour in neighbours:
            if neighbour.height > current_node.height + 1 or neighbour in closed_nodes:
                continue

            if current_node.g_cost + 1 < neighbour.g_cost or neighbour not in open_nodes:
                neighbour.g_cost = current_node.g_cost + 1
                neighbour.set_h_cost(end)

                neighbour.parent = current_node

                if neighbour not in open_nodes:
                    open_nodes.add(neighbour)


def solution_1():
    print(pathfinder(height_map, start, end))


def solution_2():
    possible_starts = [row[0] for row in height_map]
    print(min(map(lambda node: pathfinder(height_map, (node.row, node.col), end), possible_starts)))


height_map: list[list[str]] = [[char for char in row.strip()] for row in input_txt]

start = (0, 0)
end = (0, 0)

for row in range(len(height_map)):
    for col in range(len(height_map[row])):
        if height_map[row][col] == "S":
            height_map[row][col] = Node(0, row, col)
            start = (row, col)

        elif height_map[row][col] == "E":
            height_map[row][col] = Node(25, row, col)
            end = (row, col)

        else:
            height_map[row][col] = Node(ord(height_map[row][col]) - 97, row, col)

height_map: list[list[Node]]

solution_2()
