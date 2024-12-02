
with open("input.txt") as file:
    inp = file.read().splitlines()


def safe(nums):
    sorted_nums = sorted(nums)
    if nums not in [sorted_nums, sorted_nums[::-1]]:
        return 0

    diff = [sorted_nums[i] - sorted_nums[i - 1] for i in range(1, len(nums))]
    if min(diff) == 0 or max(diff) > 3:
        return 0

    return 1


def safe2(nums, fault=False):
    diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    if sum(diff) / len(diff) < 0:
        nums = nums[::-1]

    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i] or nums[i] - nums[i - 1] > 3 or nums[i] - nums[i - 1] == 0:
            if fault:
                return 0

            return safe2(nums[:i - 1] + nums[i:], fault=True) or safe2(nums[:i] + nums[i + 1:], fault=True)

    return 1


inp = [list(map(int, row.split())) for row in inp]
print(sum(safe(nums) for nums in inp))
print(sum(safe2(nums) for nums in inp))
