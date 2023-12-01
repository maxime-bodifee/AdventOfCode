import sympy

with open("input.txt") as file:
    monkeys = {}
    [monkeys.update({row[:4]: row[5:].strip().split()}) for row in file]


def yell(m: str, p2=False):
    if m == "root" and p2:
        return yell(monkeys[m][0], p2), yell(monkeys[m][2], p2)

    elif m == "humn" and p2:
        return "humn"

    elif "+" in monkeys[m]:
        return f"({yell(monkeys[m][0], p2)} + {yell(monkeys[m][2], p2)})"

    elif "-" in monkeys[m]:
        return f"({yell(monkeys[m][0], p2)} - {yell(monkeys[m][2], p2)})"

    elif "*" in monkeys[m]:
        return f"({yell(monkeys[m][0], p2)} * {yell(monkeys[m][2], p2)})"

    elif "/" in monkeys[m]:
        return f"({yell(monkeys[m][0], p2)} / {yell(monkeys[m][2], p2)})"

    else:
        return monkeys[m][0]


def part_1():
    return round(eval(yell("root")))


def part_2():
    eq = yell("root", p2=True)
    humn = sympy.Symbol("humn")

    return round(sympy.solvers.solve(sympy.Eq(eval(eq[0]), eval(eq[1])), humn)[0])


print(part_1())
print(part_2())
