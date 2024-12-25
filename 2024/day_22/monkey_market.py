from collections import defaultdict
from itertools import pairwise


def mix_and_prune(secret_number, result):
    return (secret_number ^ result) % 16_777_216


def generate_secret_number(secret_number):
    secret_number = mix_and_prune(secret_number, secret_number * 64)
    secret_number = mix_and_prune(secret_number, secret_number // 32)
    return mix_and_prune(secret_number, secret_number * 2048)


with open("input.txt") as file:
    nums = list(map(int, file.read().splitlines()))

total = 0
diffs = []

for num in nums:
    secret_nums = [num]
    for _ in range(2000):
        num = generate_secret_number(num)
        secret_nums.append(num)

    total += num
    diffs.append([(m % 10, m % 10 - n % 10) for n, m in pairwise(secret_nums)])

print(total)

all_sequences = defaultdict(int)

for diff in diffs:
    sequences = {}
    for i in range(len(diff) - 3):
        sequence = tuple([d for _, d in diff[i:i + 4]])
        bananas = diff[i + 3][0]
        if sequence not in sequences:
            sequences[sequence] = bananas

    for k, v in sequences.items():
        all_sequences[k] += v

print(max(all_sequences.values()))
