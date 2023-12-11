

def sum_min_paths(expansion_factor):
    ix_h = [i for i, row in enumerate(inp) if all(char == "." for char in row)]
    ix_v = [j for j in range(len(inp[0])) if all(row[j] == "." for row in inp)]

    g = [(x, y) for y, row in enumerate(inp) for x, char in enumerate(row) if char == "#"]
    s = 0
    for i, (x1, y1) in enumerate(g):
        for j, (x2, y2) in enumerate(g[i + 1:]):
            ih = [ix for ix in ix_h if min(y1, y2) < ix < max(y1, y2)]
            iv = [ix for ix in ix_v if min(x1, x2) < ix < max(x1, x2)]
            s += abs(y2 - y1) + abs(x2 - x1) + (expansion_factor - 1) * (len(ih) + len(iv))

    return s


if __name__ == "__main__":
    with open("input.txt") as file:
        inp = file.read().splitlines()

    print(sum_min_paths(2))
    print(sum_min_paths(1_000_000))
