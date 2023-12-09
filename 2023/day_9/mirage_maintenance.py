from collections import deque


def get_next(initial):
    all_lists, next_list = [deque(initial)], deque(initial)

    while any(next_list):
        next_list = deque(next_list[i + 1] - next_list[i] for i in range(len(next_list) - 1))
        all_lists.append(next_list)

    for i in range(len(all_lists) - 2, -1, -1):
        all_lists[i].append(all_lists[i][-1] + all_lists[i + 1][-1])
        all_lists[i].appendleft(all_lists[i][0] - all_lists[i + 1][0])

    return all_lists[0][-1], all_lists[0][0]


def main(filename="input.txt"):
    with open(filename) as file:
        input_txt = [list(map(int, line.split())) for line in file.read().splitlines()]

    part_1, part_2 = zip(*(get_next(line) for line in input_txt))

    print(sum(part_1), sum(part_2))


if __name__ == "__main__":
    main()
