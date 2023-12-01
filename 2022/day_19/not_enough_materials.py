import numpy as np
from typing import Self

MATERIALS = ["ore", "clay", "obsidian", "geode"]
max_geodes = 0


class Blueprint:
    def __init__(self: Self, bp_id: int, robots: dict[str, dict[str, int]], max_costs: dict[str, int]) -> None:
        self.id = bp_id
        self.robots = robots
        self.max_costs = max_costs

    def geodes(self, robots: dict, materials: dict, last: str | None, time: int) -> int:
        global max_geodes

        if time == 0:
            return materials["geode"]

        if max_geodes - materials["geode"] >= (time * (2 * robots["geode"] + time - 1)) // 2:
            return 0

        wait = False

        for mat, cost in self.robots.items():
            if mat != "geode" and time * robots[mat] + materials[mat] > time * self.max_costs[mat]:
                continue

            if last in [mat, None] and all(v <= materials[m] - robots[m] for m, v in cost.items()):
                continue

            if any(materials[m] < v for m, v in cost.items()):
                wait = wait or all(robots[m] > 0 for m in cost.keys())
                continue

            next_materials = {m: v + robots[m] - cost.get(m, 0) for m, v in materials.items()}
            next_robots = {m: v + int(m == mat) for m, v in robots.items()}

            max_geodes = max(max_geodes, self.geodes(next_robots, next_materials, mat, time - 1))

        if wait:
            next_materials = {mat: value + robots[mat] for mat, value in materials.items()}

            max_geodes = max(max_geodes, self.geodes(robots, next_materials, None, time - 1))

        return max_geodes


def create_blueprints(filename: str) -> list[Blueprint]:
    blueprints = []

    with open(filename) as file:
        for row in file:
            row = row.split(": ")

            bp_id = int(row[0].split()[-1])

            robots = {}
            for mat, costs in [item[5:].split(" robot costs ") for item in row[1].strip(".\n").split(". ")]:
                robots[mat] = {mat: int(value) for value, mat in (cost.split() for cost in costs.split(" and "))}

            max_costs = {mat: max(costs.get(mat, 0) for costs in robots.values()) for mat in robots.keys()}

            blueprints.append(Blueprint(bp_id, robots, max_costs))

    return blueprints


def part_1(blueprints: list[Blueprint]) -> int:
    global max_geodes

    quality_levels = []

    for bp in blueprints:
        max_geodes = 0

        robots = {mat: 0 + int(mat == "ore") for mat in MATERIALS}
        materials = {mat: 0 for mat in MATERIALS}

        quality_levels.append(bp.id * bp.geodes(robots, materials, None, 24))

    return sum(quality_levels)


def part_2(blueprints: list[Blueprint]) -> int:
    global max_geodes

    geodes_opened = []

    for bp in blueprints[:3]:
        max_geodes = 0

        robots = {mat: 0 + int(mat == "ore") for mat in MATERIALS}
        materials = {mat: 0 for mat in MATERIALS}

        geodes_opened.append(bp.geodes(robots, materials, None, 32))

    return np.product(geodes_opened)


blueprints = create_blueprints("input.txt")

print(part_1(blueprints))
print(part_2(blueprints))
