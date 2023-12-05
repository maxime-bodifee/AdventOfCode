

def part_1():
    v = vals
    for mapping in mappings:
        new_v = []

        for val in v:
            mapped = False
            for d, s, r in mapping:
                if s <= val <= s + r:
                    new_v.append(d + val - s)
                    mapped = True
                    break

            if not mapped:
                new_v.append(val)

        v = new_v

    return min(v)


def part_2():
    v = [(vals[i], vals[i] + vals[i + 1] - 1) for i in range(0, len(vals), 2)]
    m = [[(s, s + r - 1, d, d + r - 1) for d, s, r in mapping] for mapping in mappings]
    for mapping in m:
        new_v = []
        process = v
        while process:
            x, y = process.pop()
            mapped = False
            for s, t, d, e in mapping:
                if y < s or x > t:
                    continue

                if x >= s:
                    new_v.append((d + x - s, min(d + y - s, d + t - s)))
                    if y > t:
                        process.append((t + 1, y))

                elif x < s:
                    process.append((x, s - 1))
                    new_v.append((d, min(d + y - s, e)))
                    if y > t:
                        process.append((t + 1, y))

                mapped = True
                break

            if not mapped:
                new_v.append((x, y))

        v = list(set(new_v))

    return min(v)[0]


with open("input.txt") as file:
    vals, *input_txt = [line.strip("\n") for line in file.readlines()]

vals = list(map(int, vals.strip("seeds: ").split()))

ind = [i for i, x in enumerate(input_txt) if x == ""] + [-1]
mappings = []
for i in range(len(ind) - 1):
    mappings.append([list(map(int, line.split())) for line in input_txt[ind[i] + 2:ind[i + 1]]])

print(part_1())
print(part_2())
