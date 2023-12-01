from collections import deque

with open("input.txt") as file:
    jet_pattern = file.readline()


class Chamber:
    def __init__(self):
        self.rocks = [["#"] * 9]
        self.rocks_fallen = 0
        self.prev_rocks = deque()
        self.height = 0
        self.height_offset = 0
        self.jet_id = 0
        self.states = {}

    def generate_key(self, rock: "Rock") -> int | None:
        self.prev_rocks.appendleft(rock.coords[0][0] + rock.rock_id * 7 + (self.jet_id % len(jet_pattern)) * 7 * 5)

        if len(self.prev_rocks) < 3:
            return None

        while len(self.prev_rocks) > 3:
            self.prev_rocks.pop()

        return self.prev_rocks[0] + self.prev_rocks[1] * 2 + self.prev_rocks[2] * 3

    def check_for_cycle(self, rocks: int, key: int | None) -> None:
        if key is None:
            return

        if key in self.states:
            rocks_fallen, height = self.states[key]
            cycle_period = self.rocks_fallen - rocks_fallen

            cycles = (rocks - rocks_fallen) // cycle_period

            self.rocks_fallen = cycles * cycle_period + rocks_fallen
            self.height_offset = (cycles - 1) * (self.height - height)

            self.states.clear()

        else:
            self.states[key] = (self.rocks_fallen, self.height)

    def simulate_rocks(self, rocks: int) -> int:
        while self.rocks_fallen < rocks:
            rock = Rock(self.rocks_fallen % 5, self.height)

            while len(self.rocks) <= self.height + 7:
                self.rocks.append(["#"] + ['.'] * 7 + ["#"])

            while True:
                rock.jet_push(self, jet_pattern[self.jet_id % len(jet_pattern)])
                self.jet_id += 1

                if not rock.move_down(self):
                    self.height = rock.max_height() if rock.max_height() > self.height else self.height
                    break

            key = self.generate_key(rock)
            self.check_for_cycle(rocks, key)

            self.rocks_fallen += 1

        return self.height + self.height_offset


class Rock:
    def __init__(self, rock_id: int, h: int) -> None:
        self.rock_id = rock_id

        match self.rock_id:
            case 0:
                self.coords = [[3, h + 4], [4, h + 4], [5, h + 4], [6, h + 4]]

            case 1:
                self.coords = [[4, h + 4], [3, h + 5], [4, h + 5], [5, h + 5], [4, h + 6]]

            case 2:
                self.coords = [[3, h + 4], [4, h + 4], [5, h + 4], [5, h + 5], [5, h + 6]]

            case 3:
                self.coords = [[3, h + 4], [3, h + 5], [3, h + 6], [3, h + 7]]

            case 4:
                self.coords = [[3, h + 4], [4, h + 4], [3, h + 5], [4, h + 5]]

    def max_height(self) -> int:
        return max(y for _, y in self.coords)

    def jet_push(self, chamber: Chamber, jet: str) -> None:
        if jet == "<" and not any(chamber.rocks[y][x - 1] == "#" for x, y in self.coords):
            self.coords = [[x - 1, y] for x, y in self.coords]

        elif jet == ">" and not any(chamber.rocks[y][x + 1] == "#" for x, y in self.coords):
            self.coords = [[x + 1, y] for x, y in self.coords]

    def move_down(self, chamber: Chamber) -> bool:
        if any(chamber.rocks[y - 1][x] == "#" for x, y in self.coords):
            for x, y in self.coords:
                chamber.rocks[y][x] = "#"

            return False

        else:
            self.coords = [[x, y - 1] for x, y in self.coords]

            return True


print(Chamber().simulate_rocks(2022))
print(Chamber().simulate_rocks(1_000_000_000_000))
