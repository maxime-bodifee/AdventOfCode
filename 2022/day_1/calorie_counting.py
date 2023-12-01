with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n")

calorie_list = []
calories = 0

for i in range(len(input_txt)):
    if input_txt[i] == "":
        calorie_list.append(calories)
        calories = 0

    else:
        calories += int(input_txt[i])


def solution_1():
    print(max(calorie_list))


def solution_2():
    calorie_list.sort(reverse=True)

    calories_top_3 = 0
    for i in range(3):
        calories_top_3 += calorie_list[i]

    print(calories_top_3)


solution_2()
