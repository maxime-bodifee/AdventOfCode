with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n")

with open("example.txt") as file:
    input_txt_example = file.readlines()
    for i in range(len(input_txt_example)):
        input_txt_example[i] = input_txt_example[i].strip("\n")


class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspected_items = 0

    def inspect_items_1(self):
        for i in range(len(self.items)):
            item = self.operation(self.items[i])
            item //= 3

            if item % self.test == 0:
                monkeys[self.true].items.append(item)
            else:
                monkeys[self.false].items.append(item)

            self.inspected_items += 1

        self.items = []

    def inspect_items_2(self):
        for i in range(len(self.items)):
            item = self.operation(self.items[i])
            item %= 9_699_690

            if item % self.test == 0:
                monkeys[self.true].items.append(item)
            else:
                monkeys[self.false].items.append(item)

            self.inspected_items += 1

        self.items = []


def create_monkeys():
    monkeys = []

    for i in range(0, len(input_txt), 7):
        items = [int(num) for num in input_txt[i + 1][18:].split(", ")]

        if i == 0:
            operation = lambda n: n * 7
        if i == 7:
            operation = lambda n: n + 8
        if i == 14:
            operation = lambda n: n * 13
        if i == 21:
            operation = lambda n: n + 7
        if i == 28:
            operation = lambda n: n + 2
        if i == 35:
            operation = lambda n: n + 1
        if i == 42:
            operation = lambda n: n + 4
        if i == 49:
            operation = lambda n: n ** 2

        test = int(input_txt[i + 3].split()[-1])

        true = int(input_txt[i + 4].split()[-1])
        false = int(input_txt[i + 5].split()[-1])

        monkeys.append(Monkey(items, operation, test, true, false))

    return monkeys


def create_monkeys_example():
    monkeys = []

    for i in range(0, len(input_txt_example), 7):
        items = [int(num) for num in input_txt_example[i + 1][18:].split(", ")]

        if i == 0:
            operation = lambda n: n * 19
        if i == 7:
            operation = lambda n: n + 6
        if i == 14:
            operation = lambda n: n ** 2
        if i == 21:
            operation = lambda n: n + 3

        test = int(input_txt[i + 3].split()[-1])

        true = int(input_txt[i + 4].split()[-1])
        false = int(input_txt[i + 5].split()[-1])

        monkeys.append(Monkey(items, operation, test, true, false))

    return monkeys


def solution_1():
    for _ in range(20):
        for i in range(len(monkeys)):
            monkeys[i].inspect_items_1()

    inspected_items = sorted(map(lambda m: m.inspected_items, monkeys), reverse=True)

    print(inspected_items[0] * inspected_items[1])


def solution_2():
    for _ in range(10000):
        for i in range(len(monkeys)):
            monkeys[i].inspect_items_2()

    inspected_items = sorted(map(lambda m: m.inspected_items, monkeys), reverse=True)

    print(inspected_items[0] * inspected_items[1])


monkeys = create_monkeys()
solution_2()
