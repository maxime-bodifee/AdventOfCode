import re
import numpy as np

with open("input.txt") as file:
    inp = file.read().splitlines()


def count_xmas(grid):
    return sum(len(re.findall("XMAS", "".join(row))) + len(re.findall("SAMX", "".join(row))) for row in grid)


grid = np.array([list(row) for row in inp])
dim = grid.shape[0]

inp_d1 = []
for i in range(-dim + 1, dim):
    inp_d1.append(grid.diagonal(i).tolist())

inp_d2 = []
for i in range(-dim + 1, dim):
    inp_d2.append(np.fliplr(grid).diagonal(i).tolist())


print(count_xmas(grid.tolist()) + count_xmas(grid.T.tolist()) + count_xmas(inp_d1) + count_xmas(inp_d2))


x_mas = ["MMASS", "MSAMS", "SMASM", "SSAMM"]
total = 0

for i in range(dim - 2):
    for j in range(dim - 2):
        if inp[i][j] + inp[i][j + 2] + inp[i + 1][j + 1] + inp[i + 2][j] + inp[i + 2][j + 2] in x_mas:
            total += 1

print(total)
