import math as m

with open("input.txt") as file:
    fuels = [row.strip() for row in file]

fuel_total = 0

for fuel in fuels:
    for i, char in enumerate(reversed(fuel)):
        match char:
            case "2":
                fuel_total += 2 * (5 ** i)

            case "1":
                fuel_total += (5 ** i)

            case "-":
                fuel_total -= (5 ** i)

            case "=":
                fuel_total -= 2 * (5 ** i)

snafu_num = ""

for i in range(m.floor(m.log(fuel_total, 5)), -1, -1):
    match round(fuel_total / 5 ** i):
        case 2:
            snafu_num += "2"
            fuel_total -= 2 * 5 ** i

        case 1:
            snafu_num += "1"
            fuel_total -= 1 * 5 ** i

        case 0:
            snafu_num += "0"

        case -1:
            snafu_num += "-"
            fuel_total += 5 ** i

        case -2:
            snafu_num += "="
            fuel_total += 2 * 5 ** i

print(snafu_num)
