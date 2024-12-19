from collections import defaultdict

with open("input.txt") as file:
    towels, designs = file.read().split("\n\n")
    towels, designs = towels.split(", "), designs.splitlines()

memo_1 = defaultdict(bool)
memo_2 = defaultdict(int)


def possible_design(design):
    if design == "":
        return True
    if design in memo_1:
        return memo_1[design]

    possible = False
    for towel in towels:
        if design.startswith(towel) and possible_design(design[len(towel):]):
            possible = True

    memo_1[design] = possible
    return possible


def count_designs(design):
    if design == "":
        return True
    if design in memo_2:
        return memo_2[design]

    count = 0
    for towel in towels:
        if design.startswith(towel):
            count += count_designs(design[len(towel):])

    memo_2[design] = count
    return count


print(sum(possible_design(design) for design in designs))
print(sum(count_designs(design) for design in designs))
