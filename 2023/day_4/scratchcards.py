with open("input.txt") as file:
    s = [line.strip('\n').split()[2:] for line in file.readlines()]

total_score = 0
total_cards = [1] * len(s)

for i, line in enumerate(s):
    win = []
    while line[0] != '|':
        win.append(int(line[0]))
        line = line[1:]

    win_nums = sum(1 if int(num) in win else 0 for num in line[1:])
    total_score += 2 ** (win_nums - 1) if win_nums > 0 else 0
    for j in range(win_nums):
        total_cards[i + j + 1] += total_cards[i]

print(total_score, sum(total_cards))
