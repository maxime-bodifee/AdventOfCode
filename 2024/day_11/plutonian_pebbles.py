from collections import defaultdict


def blink(stones: dict[int, int], blinks: int) -> int:
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for num, count in stones.items():
            if num == 0:
                new_stones[1] += count
            elif (num_len := len(num_str := str(num))) % 2 == 0:
                new_stones[int(num_str[:num_len // 2])] += count
                new_stones[int(num_str[num_len // 2:])] += count
            else:
                new_stones[num * 2024] += count

        stones = new_stones

    return sum(stones.values())


with open("input.txt") as file:
    inp = {int(num): 1 for num in file.read().split()}


print(blink(inp.copy(), 25))
print(blink(inp.copy(), 75))
