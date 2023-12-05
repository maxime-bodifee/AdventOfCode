

def part_1():
    v = vals
    for mapping in mappings:
        new_v = []

        for val in v:
            for d, s, r in mapping:
                if s <= val <= s + r:
                    new_v.append(d + val - s)
                    break

            else:
                new_v.append(val)

        v = new_v

    return min(v)


def part_2():
    v = [(vals[i], vals[i] + vals[i + 1] - 1) for i in range(0, len(vals), 2)]
    m = [[(s, s + r - 1, d, d + r - 1) for d, s, r in mapping] for mapping in mappings]
    for mapping in m:
        new_v = []
        q = v
        while q:
            x, y = q.pop()
            for s, t, d, e in mapping:
                if y < s or x > t:
                    continue
                if x < s:
                    q.append((x, s - 1))
                if y > t:
                    q.append((t + 1, y))
                new_v.append((max(d, d + x - s), min(d + y - s, e)))
                break

            else:
                new_v.append((x, y))

        v = new_v

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
