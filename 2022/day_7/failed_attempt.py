with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n")


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name


class Dir:
    def __init__(self, name, *files):
        self.name = name
        self.files = []
        for i in range(len(files)):
            if type(files[i]) == Dir:
                for j in range(i, len(files)):
                    if type(files[j]) == Dir:
                        continue
                    else:
                        self.files.append(files[j])

    def size(self):
        size = 0

        for file in self.files:
            size += file.size

        return size


commands = []
files = []
dirs = []

for i in range(len(input_txt)):
    if input_txt[i][0] == "$":
        commands.append(input_txt[i].strip("$ "))

    else:
        files.append(input_txt[i])

for i, file in enumerate(files):
    if file.startswith("dir "):
        continue

    else:
        file = file.split()
        file = File(file[0], file[1])

for i, file in enumerate(files):
    if type(file) != File:
        dirs.append(Dir(files))
        files.pop(i)

total_size = 0
for i in range(len(dirs)):
    size = dirs[i].size()
    if size <= 100000:
        total_size += size

print(total_size)
