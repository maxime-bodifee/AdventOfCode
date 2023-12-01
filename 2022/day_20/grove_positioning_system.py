

class Number:
    def __init__(self, value):
        self.value = value


def mix(filename, key=1, count=1):
    with open(filename) as file:
        original = [Number(int(num) * key) for num in file]

    nums = original.copy()

    for _ in range(count):
        for num in original:
            i = nums.index(num)
            new_i = (i + num.value) % (len(nums) - 1)

            nums.insert(new_i, nums.pop(i))

    i_0 = nums.index(list(filter(lambda n: n.value == 0, nums))[0])

    return sum([nums[(i_0 + i) % len(nums)].value for i in range(1000, 3001, 1000)])


def part_1():
    return mix("input.txt")


def part_2():
    return mix("input.txt", key=811589153, count=10)


print(part_1())
print(part_2())
