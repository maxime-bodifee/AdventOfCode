

def find_S():
    for i, row in enumerate(inp):
        for j, char in enumerate(row):
            if inp[i][j] == "S":
                return complex(j, i)


with open("input.txt") as file:
    inp = file.read().splitlines()

# {(char, direction): new_direction}
m = {
    ("L", 1j): 1, ("L", -1): -1j,
    ("J", 1j): -1, ("J", 1): -1j,
    ("7", 1): 1j, ("7", -1j): -1,
    ("F", -1): 1j, ("F", -1j): 1
}

# determine a valid direction based on the input
d = 1

start_p = find_S()
p = start_p + d
t = [p]
s = 1

while p != start_p:
    x, y = int(p.real), int(p.imag)
    if inp[y][x] not in ["|", "-"]:
        d = m[(inp[y][x], d)]

    p += d
    t.append(p)
    s += 1

print(s // 2)

# https://en.wikipedia.org/wiki/Shoelace_formula
a = sum((t[i].imag + t[i + 1].imag) * (t[i].real - t[i + 1].real) for i in range(len(t) - 1))
a += (t[-1].imag + t[0].imag) * (t[-1].real - t[0].real)

# https://en.wikipedia.org/wiki/Pick's_theorem
print(int((a - s) / 2) + 1)
