import functools

with open("input.txt") as file:
    input_txt = [row.strip() for row in file.readlines()]


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True

        elif left == right:
            return None

        else:
            return False

    elif type(left) == list and type(right) == list:
        for pair_1, pair_2 in zip(left, right):
            sort = compare(pair_1, pair_2)

            if sort is not None:
                return sort

        if len(left) < len(right):
            return True

        elif len(right) < len(left):
            return False

        else:
            return None

    elif type(left) == int and type(right) == list:
        return compare([left], right)

    elif type(left) == list and type(right) == int:
        return compare(left, [right])


def solution_1(input_txt):
    pairs = []

    for i in range(0, len(input_txt), 3):
        pairs.append([eval(input_txt[i]), eval(input_txt[i + 1])])

    print(sum([i + 1 for i in range(len(pairs)) if compare(pairs[i][0], pairs[i][1])]))


def solution_2(input_txt):
    packets = [[[2]], [[6]]]

    for i in range(0, len(input_txt), 3):
        packets.append(eval(input_txt[i]))
        packets.append(eval(input_txt[i + 1]))

    packets.sort(key=functools.cmp_to_key(lambda left, right: -1 if compare(left, right) else 1))

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


solution_2(input_txt)
