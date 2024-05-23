import math

with open("input.txt") as file:
    inp_r, inp_p = list(map(str.splitlines, file.read().split("\n\n")))

rules = {name: [s.split(":") for s in r.strip("}").split(",")] for name, r in [rule.split("{") for rule in inp_r]}
parts = [[int(v[2:]) for v in part.strip("{}").split(",")] for part in inp_p]


def rating(rule: str, part: list[int]) -> int:
    if rule in ["A", "R"]:
        return sum(part) if rule == "A" else 0

    for *c, r in rules[rule]:
        if not c:
            return rating(r, part)

        ch, op, *v = c[0]
        v = int("".join(v))
        i = "xmas".index(ch)
        if (op == "<" and part[i] < int(v)) or (op == ">" and part[i] > int(v)):
            return rating(r, part)


def walk(rule: str, part: list[tuple[int, int]]) -> int:
    if rule in ["A", "R"]:
        return math.prod([hi - lo + 1 for lo, hi in part]) if rule == "A" else 0

    t = 0

    for *c, r in rules[rule]:
        if not c:
            t += walk(r, part)
            break

        ch, op, *v = c[0]
        v = int("".join(v))
        i = "xmas".index(ch)
        p = part[i]
        if (op == "<" and p[1] < v) or (op == ">" and p[0] > v):
            t += walk(r, part)
            break
        if p[0] <= v <= p[1]:
            new_parts = part.copy()
            new_parts[i] = (v + 1, p[1]) if op == ">" else (part[i][0], v - 1)
            part[i] = (p[0], v) if op == ">" else (v, part[i][1])
            t += walk(r, new_parts)

    return t


def part_1():
    return sum(rating("in", part) for part in parts)


def part_2():
    return walk("in", [(1, 4000)] * 4)


print(part_1())
print(part_2())
