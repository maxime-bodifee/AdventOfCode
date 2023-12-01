import re


def part_1(txt):
    nums = ["".join(re.findall(r"\d+", line)) for line in txt]
    return sum(int(num[0] + num[-1]) for num in nums)


def part_2(txt):
    word_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, word in enumerate(word_nums, 1):
        txt = [line.replace(word, word[0] + str(num) + word[-1]) for line in txt]

    return part_1(txt)


if __name__ == "__main__":
    with open("input.txt") as file:
        input_txt = file.readlines()

    print(part_1(input_txt))
    print(part_2(input_txt))
