with open("input.txt") as file:
    input_txt = [row.strip().split() for row in file.readlines()]


def solution_1():
    points = set()

    for row in input_txt:
        sx = int(row[2].strip("x=,"))
        sy = int(row[3].strip("y=:"))

        bx = int(row[8].strip("x=,"))
        by = int(row[9].strip("y="))

        important_row = 2_000_000

        md = abs(sx - bx) + abs(sy - by)

        if sy - md < important_row < sy + md:
            dx = abs(md - abs(important_row - sy))

            for i in range(sx - dx, sx + dx):
                points.add(i)

    print(len(points))


def valid(x, y):
    return 0 <= x <= 4_000_000 and 0 <= y <= 4_000_000


def solution_2():
    sensors = {}
    valid_pos = set()

    for row in input_txt:
        sx = int(row[2].strip("x=,"))
        sy = int(row[3].strip("y=:"))

        bx = int(row[8].strip("x=,"))
        by = int(row[9].strip("y="))

        md = abs(sx - bx) + abs(sy - by)

        sensors[(sx, sy)] = md

        if valid(sx, sy - md - 1):
            valid_pos.add((sx, sy - md - 1))

        if valid(sx, sy + md + 1):
            valid_pos.add((sx, sy + md + 1))

        for y in range(sy - md, sy + md):
            x_left = sx - md - abs(sy - y) - 1
            x_right = sx + md - abs(sy - y) + 1

            if valid(x_left, y):
                valid_pos.add((x_left, y))

            if valid(x_right, y):
                valid_pos.add((x_right, y))

    for pos in valid_pos:
        inside_sensor_range = len(sensors)

        for sensor, md in sensors.items():
            if abs(sensor[0] - pos[0]) + abs(sensor[1] - pos[1]) > md:
                inside_sensor_range -= 1

            else:
                break

        if inside_sensor_range == 0:
            print(pos[0] * 4_000_000 + pos[1])
            break


solution_2()
