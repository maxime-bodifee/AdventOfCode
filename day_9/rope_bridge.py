with open("input.txt") as file:
    input_txt = file.readlines()
    for i in range(len(input_txt)):
        input_txt[i] = input_txt[i].strip("\n").split()

X = 0
Y = 1


def solution_1():
    head = [0, 0]
    tail = [0, 0]
    positions = []

    for i in range(len(input_txt)):
        direction = input_txt[i][0]
        distance = int(input_txt[i][1])

        for j in range(distance):
            if direction == "R":
                head[X] += 1

            elif direction == "L":
                head[X] -= 1

            elif direction == "U":
                head[Y] += 1

            elif direction == "D":
                head[Y] -= 1

            dx = head[X] - tail[X]
            dy = head[Y] - tail[Y]

            if abs(dx) == 2:
                if dx > 0:
                    tail[X] += 1
                else:
                    tail[X] -= 1

                if dy == 1:
                    tail[Y] += 1
                elif dy == -1:
                    tail[Y] -= 1

            elif abs(dy) == 2:
                if dy > 0:
                    tail[Y] += 1
                else:
                    tail[Y] -= 1

                if dx == 1:
                    tail[X] += 1
                elif dx == -1:
                    tail[X] -= 1

            if tail not in positions:
                positions.append(tail.copy())

    print(len(positions))


def solution_2():
    knots = [[0, 0] for _ in range(10)]
    tail_positions = []

    for i in range(len(input_txt)):
        direction = input_txt[i][0]
        distance = int(input_txt[i][1])

        for j in range(distance):
            match direction:
                case "R":
                    knots[0][X] += 1

                case "L":
                    knots[0][X] -= 1

                case "U":
                    knots[0][Y] += 1

                case "D":
                    knots[0][Y] -= 1

            for k in range(9):
                head = knots[k]
                tail = knots[k + 1]

                dx = head[X] - tail[X]
                dy = head[Y] - tail[Y]

                if abs(dx) != 2 and abs(dy) != 2:
                    continue

                # clamp
                dx = max(min(dx, 1), -1)
                dy = max(min(dy, 1), -1)

                tail[X] += dx
                tail[Y] += dy

            if knots[-1] not in tail_positions:
                tail_positions.append(knots[-1].copy())

    print(tail_positions)
    print(len(tail_positions))


solution_2()
