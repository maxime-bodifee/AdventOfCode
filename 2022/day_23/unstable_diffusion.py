from collections import defaultdict


def diffusion(filename, part=1):
    with open(filename) as file:
        input_txt = [row.strip() for row in file]

    elf_map = defaultdict(lambda: False)
    elf_map.update({(j, i): True for i, row in enumerate(input_txt) for j, char in enumerate(row) if char == "#"})

    rounds = 0

    while True:
        elf_pos = [pos for pos, elf in elf_map.items() if elf]
        new_pos = defaultdict(list)

        if rounds == 10 and part == 1:
            x = [elf[0] for elf in elf_pos]
            y = [elf[1] for elf in elf_pos]

            return (max(x) - min(x) + 1) * (max(y) - min(y) + 1) - len(elf_pos)

        for elf in elf_pos:
            if not any(elf_map[elf[0] + dx, elf[1] + dy]
                       for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0):
                continue

            for i in range(4):
                dir = (rounds + i) % 4

                match dir:
                    case 0:  # north
                        if not any([elf_map[elf[0] + dx, elf[1] - 1] for dx in [-1, 0, 1]]):
                            new_pos[elf[0], elf[1] - 1].append(elf)
                            break

                    case 1:  # south
                        if not any([elf_map[elf[0] + dx, elf[1] + 1] for dx in [-1, 0, 1]]):
                            new_pos[elf[0], elf[1] + 1].append(elf)
                            break

                    case 2:  # west
                        if not any([elf_map[elf[0] - 1, elf[1] + dy] for dy in [-1, 0, 1]]):
                            new_pos[elf[0] - 1, elf[1]].append(elf)
                            break

                    case 3:  # east
                        if not any([elf_map[elf[0] + 1, elf[1] + dy] for dy in [-1, 0, 1]]):
                            new_pos[elf[0] + 1, elf[1]].append(elf)
                            break

        if len(new_pos) == 0:
            return rounds + 1

        for pos, elves in new_pos.items():
            if len(elves) == 1:
                elf_map[elves[0]] = False
                elf_map[pos] = True

        rounds += 1


print(diffusion("input.txt"))
print(diffusion("input.txt", part=2))
