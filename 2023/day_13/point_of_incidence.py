

def reflect(p, tol):
    for i in range(1, len(p)):
        if sum(c1 != c2 for r1, r2 in zip(p[i - 1::-1], p[i:]) for c1, c2 in zip(r1, r2)) == tol:
            return i
    else:
        return 0


with open("input.txt") as file:
    patterns = list(map(str.splitlines, file.read().split('\n\n')))

for tol in 0, 1:
    print(sum(100 * reflect(p, tol) + reflect([*zip(*p)], tol) for p in patterns))
