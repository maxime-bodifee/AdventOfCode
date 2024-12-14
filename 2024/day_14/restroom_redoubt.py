import re
from math import prod
from itertools import product

import pygame
import numpy as np

with open("input.txt") as file:
    robots = [
        list(map(int, robot))
        for robot in re.findall(".*?".join([r"(-?\d+)"] * 4), file.read())
    ]

# tx, ty = 11, 7
tx, ty = 101, 103

quadrants = [
    list(product(x, y))
    for x in [range(tx // 2), range(tx // 2 + 1, tx + 1)]
    for y in [range(ty // 2), range(ty // 2 + 1, ty + 1)]
]

for j in range(10_000):
    if j == 100:
        print(prod(sum((px, py) in quadrant for px, py, *_ in robots) for quadrant in quadrants))

    grid = np.zeros((tx, ty, 3))
    for i, (px, py, vx, vy) in enumerate(robots):
        grid[px, py] = [255, 255, 255]
        robots[i] = [(px + vx) % tx, (py + vy) % ty, vx, vy]

    pygame.image.save(
        pygame.surfarray.make_surface(grid),
        f"./seconds/{j}.png",
    )
