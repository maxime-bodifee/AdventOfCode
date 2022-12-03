with open("example.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n")

def solution_1():
    priority_list = []
    priority = 0

    for i in range(len(input_txt)):
        compartment_1 = input_txt[i][:len(input_txt[i]) // 2]
        compartment_2 = input_txt[i][len(input_txt[i]) // 2:]
        counter = 0

        for letter_1 in compartment_1:
            for letter_2 in compartment_2:
                if counter == 1:
                    continue

                elif letter_1 == letter_2:
                    priority_list.append(letter_1)
                    counter += 1

    for i in range(len(priority_list)):
        value = ord(priority_list[i])
        if value >= 97:
            priority += (value - 96)
        else:
            priority += (value - 38)

    print(priority)

def solution_2():
    priority_list = []
    priority = 0

    for i in range(0, len(input_txt), 3):
        rucksack_1 = input_txt[i]
        rucksack_2 = input_txt[i + 1]
        rucksack_3 = input_txt[i + 2]

        counter = 0

        for letter_1 in rucksack_1:
            for letter_2 in rucksack_2:
                for letter_3 in rucksack_3:
                    if counter == 1:
                        continue

                    elif letter_1 == letter_2 == letter_3:
                        priority_list.append(letter_1)

    for i in range(len(priority_list)):
        value = ord(priority_list[i])
        if value >= 97:
            priority += (value - 96)
        else:
            priority += (value - 38)

    print(priority_list)
    print(priority)

solution_2()
