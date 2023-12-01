with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip()

cwd = root = {}
stack = []

for line in input_txt:
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]

            if dir == "/":
                cwd = root
                stack = []

            elif dir == "..":
                cwd = stack.pop()

            else:
                if dir not in cwd:
                    cwd[dir] = {}

                stack.append(cwd)
                cwd = cwd[dir]

    else:
        x, y = line.split()

        if x == "dir":
            if y not in cwd:
                cwd[y] = {}

        else:
            cwd[y] = int(x)


def solution_1(dir=None):
    if dir is None:
        dir = root

    if type(dir) == int:
        return dir, 0
    size = 0
    dir_size = 0

    for child in dir.values():
        s, a = solution_1(child)
        size += s
        dir_size += a

    if size <= 100000:
        dir_size += size

    print(dir_size)


def size(dir=None):
    if dir is None:
        dir = root

    if type(dir) == int:
        return dir

    return sum(map(size, dir.values()))


t = size() - 40_000_000


def solution_2(dir=None):
    if dir is None:
        dir = root

    dir_size = float("inf")

    if size(dir) >= t:
        dir_size = size(dir)

    for child in dir.values():
        if type(child) == int:
            continue

        new_dir = solution_2(child)
        dir_size = min(dir_size, new_dir)

    return dir_size


print(solution_2())
