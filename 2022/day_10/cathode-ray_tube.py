with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n").split()


def solution_1():
    cycle = 0
    cycle_list = [20, 60, 100, 140, 180, 220]
    j = 0
    threshold = cycle_list[j]
    register = 1
    signal_strength = 0

    for i in range(len(input_txt)):
        if input_txt[i][0] == "addx":
            cycle += 2

            if cycle > 220:
                break

            elif cycle >= threshold:
                signal_strength += cycle_list[j] * register
                j += 1
                if j == 6:
                    break
                threshold = cycle_list[j]

            register += int(input_txt[i][1])

        elif input_txt[i][0] == "noop":
            cycle += 1

            if cycle > 220:
                break

            elif cycle >= threshold:
                signal_strength += cycle_list[j] * register
                j += 1
                if j == 6:
                    break
                threshold = cycle_list[j]

    print(signal_strength)


def solution_1_v2():
    cycle = 1
    register = 1
    cycle_list = [i * 40 + 20 for i in range(6)]
    index = 0
    threshold = cycle_list[index]
    signal_strengths = []

    for line in input_txt:
        if line[0] == "addx":
            cycle += 2

        else:
            cycle += 1

        if cycle > threshold:
            signal_strengths += [cycle_list[index] * register]

            if index == len(cycle_list) - 1:
                break

            index += 1
            threshold = cycle_list[index]

        if line[0] == "addx":
            register += int(line[1])

    print(sum(signal_strengths))


def solution_2():
    crt_row = ["" for _ in range(40)]
    row = 0

    cycle = 1
    register = 1

    for i in range(len(input_txt)):
        if input_txt[i][0] == "addx":
            position = cycle - 1 - (row * 40)

            if cycle > 240:
                break

            elif position == register - 1 or position == register or position == register + 1:
                crt_row[position] = "#"

            else:
                crt_row[position] = "."

            if position == 39:
                print(crt_row)
                row += 1

            cycle += 1

            position = cycle - 1 - (row * 40)

            if cycle > 240:
                break

            elif position == register - 1 or position == register or position == register + 1:
                crt_row[position] = "#"

            else:
                crt_row[position] = "."

            if position == 39:
                print(crt_row)
                row += 1

            cycle += 1

            register += int(input_txt[i][1])

        elif input_txt[i][0] == "noop":
            position = cycle - 1 - (row * 40)

            if cycle > 240:
                break

            elif position == register - 1 or position == register or position == register + 1:
                crt_row[position] = "#"

            else:
                crt_row[position] = "."

            if position == 39:
                print(crt_row)
                row += 1

            cycle += 1


def solution_2_v2():
    crt_row = ["" for _ in range(40)]
    rows_completed = 0

    position = 0
    register = 1

    for line in input_txt:
        if line[0] == "addx":
            n = 2

        else:
            n = 1

        for i in range(n):
            if position == register - 1 or position == register or position == register + 1:
                crt_row[position] = "#"

            else:
                crt_row[position] = "."

            position += 1

            if position > 39:
                print(crt_row)
                position = 0
                rows_completed += 1
                if rows_completed >= 6:
                    break

        if line[0] == "addx":
            register += int(line[1])


solution_2_v2()
