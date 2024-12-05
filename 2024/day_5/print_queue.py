with open("input.txt") as file:
    rules, updates = file.read().split("\n\n")

rules = [rule.split("|") for rule in rules.splitlines()]
updates = [update.split(",") for update in updates.splitlines()]

total_1 = 0

for update in updates:
    valid = True

    for a, b in rules:
        if a not in update or b not in update:
            continue

        if update.index(a) > update.index(b):
            valid = False
            break

    if not valid:
        continue

    total_1 += int(update[len(update) // 2])

print(total_1)


total_2 = 0

for update in updates:
    rules_with = []
    valid = True

    for a, b in rules:
        if a not in update or b not in update:
            continue

        if update.index(a) > update.index(b):
            valid = False

        rules_with.append([a, b])

    if valid:
        continue

    while any(update.index(a) > update.index(b) for a, b in rules_with):
        for a, b in rules_with:
            if (ax := update.index(a)) > (bx := update.index(b)):
                update[ax], update[bx] = update[bx], update[ax]

    total_2 += int(update[len(update) // 2])

print(total_2)
