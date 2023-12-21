from math import prod

br = "broadcaster"

with open("input.txt") as file:
    inp = [s.split(" -> ") for s in file.read().splitlines()]

# dest = {module: [type, *destination modules]}
dest = {a[1:] if a != br else a: ([a[0]] if a != br else []) + b.replace(" ", "").split(",") for a, b in inp}
ff = {a: False for a, b in dest.items() if b[0] == "%"}
conj = {a: {c: False for c, d in dest.items() if a in d} for a, b in dest.items() if b[0] == "&"}
b, ps, rx = 0, [0, 0], {a: 0 for a in conj["cs"]}
while not all(rx.values()):
    if b == 1000:
        print(prod(ps))

    b += 1
    ps[0] += 1 + len(dest["broadcaster"])
    q = [("", d, "l") for d in dest["broadcaster"]]
    while q:
        s, d, p = q.pop(0)
        if not dest.get(d):
            continue

        if dest[d][0] == "%" and p == "l":
            q.extend([(d, m, "l" if ff[d] else "h") for m in dest[d][1:]])
            ps[not ff[d]] += len(dest[d]) - 1
            ff[d] = not ff[d]

        elif dest[d][0] == "&":
            rx.update({s: b} if not rx.get(s, True) and p == "h" else {})
            conj[d][s] = p == "h"
            q.extend([(d, m, "l") for m in dest[d][1:]] if all(conj[d].values()) else [(d, m, "h") for m in dest[d][1:]])
            ps[not all(conj[d].values())] += len(dest[d]) - 1

print(prod(rx.values()))
