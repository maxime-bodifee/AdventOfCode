import re

with open("input.txt") as file:
    inp = file.read()

total_1 = 0

for row in re.findall(r"mul\(\d+,\d+\)", inp):
    a, b = re.search(r"(\d+),(\d+)", row).groups()
    total_1 += int(a) * int(b)

print(total_1)

# alternative: part 1 in a single line
print(sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", inp)))

total_2 = 0
enabled = True
for row in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", inp):
    if row == "do()":
        enabled = True
        continue
    elif row == "don't()":
        enabled = False
        continue

    if not enabled:
        continue

    a, b = re.search(r"(\d+),(\d+)", row).groups()
    total_2 += int(a) * int(b)

print(total_2)
