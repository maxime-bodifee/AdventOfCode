from collections import defaultdict
from math import prod

with open("input.txt") as file:
    s = [[char for char in line.strip("\n")] for line in file.readlines()]

ans1 = 0
num_chars = "0123456789"
gears = defaultdict(list)

for i, line in enumerate(s):
    for j, char in enumerate(line):
        if char in num_chars and ((j == 0) or (j - 1 >= 0 and s[i][j - 1] not in num_chars)):
            num = ""
            k = j
            while k < len(line) and s[i][k] in num_chars:
                num += s[i][k]
                k += 1

            neighbours = [(j + dx, i + dy) for dx in range(-1, len(num) + 1) for dy in range(-1, 2)
                          if not (dy == 0 and 0 <= dx < len(num)) and 0 <= i + dy < len(s) and 0 <= j + dx < len(line)]

            for x, y in neighbours:
                if s[y][x] == "*":
                    gears[(x, y)].append(int(num))

                if s[y][x] != ".":
                    ans1 += int(num)
                    break

ans2 = 0
for gear, nums in gears.items():
    if len(nums) == 2:
        ans2 += prod(nums)

print(ans1, ans2)
