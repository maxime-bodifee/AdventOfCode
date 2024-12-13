import re
import numpy as np


def tokens(machine, offset=0):
    ax, ay, bx, by, px, py = map(int, machine)
    m = np.array([[ax, bx],
                  [ay, by]])
    p = np.array([px, py]) + offset

    x = np.linalg.solve(m, p).round().astype(int)
    return x @ [3, 1] if (m @ x == p).all() else 0


with open("input.txt") as file:
    machines = re.findall(".*?".join([r"(\d+)"] * 6), file.read(), re.DOTALL)

print(sum(tokens(machine) for machine in machines))
print(sum(tokens(machine, offset=10_000_000_000_000) for machine in machines))
