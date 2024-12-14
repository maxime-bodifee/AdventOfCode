import re
import os
from math import prod
from itertools import product
from PIL import Image, ImageDraw, ImageFont
import pygame
import numpy


def save_image(pixels, filename):
    nparray = numpy.asarray(pixels).transpose(1, 0, 2)
    surf = pygame.surfarray.make_surface(nparray)
    (width, height, colours) = nparray.shape
    surf = pygame.display.set_mode((width, height))
    pygame.surfarray.blit_array(surf, nparray)
    pygame.image.save(surf, filename)


with open("input.txt") as file:
    robots = [
        list(map(int, robot))
        for robot in re.findall(".*?".join([r"(-?\d+)"] * 4), file.read(), re.DOTALL)
    ]

# tx, ty = 11, 7
tx, ty = 101, 103

q = [
    list(product(range(tx // 2), range(ty // 2))),
    list(product(range(tx // 2), range(ty // 2 + 1, ty + 1))),
    list(product(range(tx // 2 + 1, tx + 1), range(ty // 2))),
    list(product(range(tx // 2 + 1, tx + 1), range(ty // 2 + 1, ty + 1))),
]

ql = [0, 0, 0, 0]

for j in range(10_000):
    if j == 100:
        for *pos, _, _ in robots:
            for i, qpos in enumerate(q):
                if tuple(pos) in qpos:
                    ql[i] += 1

        print(prod(ql))

    grid = [[[0, 0, 0] for _ in range(tx)] for _ in range(ty)]
    for i, (px, py, vx, vy) in enumerate(robots):
        if grid[py][px] == [0, 0, 0]:
            grid[py][px] = [255, 255, 255]

        robots[i] = [(px + vx) % tx, (py + vy) % ty, vx, vy]

    save_image(grid, f"./frames/frame{j}.png")
