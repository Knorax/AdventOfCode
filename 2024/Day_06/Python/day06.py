
from enum import Enum

OBSTACLE = "#"

class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

class Guard:
    def __init__(self, x_start = 0, y_start = 0, dir_start = Direction.N, area_map = None) -> None:
        self.x = x_start
        self.y = y_start
        self.starting_x = x_start
        self.starting_y = y_start
        self.direction: Direction = dir_start
        self.totalStepTaken = 0
        self.path = []
        self.nb_loops = 0 
        if area_map != None:
            # Create a 2D matrix the same size as the map containing lists 
            self.path = [ [ [] for _ in range(len(area_map[0])) ] for _ in range(len(area_map)) ]

    def __repr__(self) -> str:
        return f"({self.x},{self.y}) in {self.direction}"

    def nextMove(self, area_map):
        if self.obstacleAhead(area_map):
            self.rotateRight()
            self.nextMove(area_map)
        else:
            area_map[self.y] = area_map[self.y][:self.x] + "X" + area_map[self.y][self.x + 1:]
            if len(self.path) > 0:
                self.path[self.y][self.x].append(self.direction)

                if len(self.path[self.y][self.x]) > 1:
                    dir_90Deg = self.get90DegreesDirection(self.direction)

                    next_x, next_y = self.getNextSqure()
                    if dir_90Deg in self.path[self.y][self.x] and next_x != self.starting_x and next_y != self.starting_y:
                        self.nb_loops = self.nb_loops + 1

            self.moveForward()
            self.totalStepTaken = self.totalStepTaken + 1

    def obstacleAhead(self, area_map):
        match self.direction:
            case Direction.N:
                if self.y - 1 >= 0 and area_map[self.y - 1][self.x] == OBSTACLE:
                    return True
            case Direction.S:
                if self.y + 1 < len(area_map) and area_map[self.y + 1][self.x] == OBSTACLE:
                    return True
            case Direction.W:
                if self.x - 1 >= 0 and area_map[self.y][self.x - 1] == OBSTACLE:
                    return True
            case Direction.E:
                if self.x + 1 < len(area_map[0]) and area_map[self.y][self.x + 1] == OBSTACLE:
                    return True
        return False 

    def rotateRight(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def get90DegreesDirection(self, dir: Direction):
        return Direction((dir.value + 1) % 4)

    def getNextSqure(self):
        match self.direction:
            case Direction.N:
                return self.x, self.y - 1
            case Direction.S:
                return self.x, self.y + 1
            case Direction.W:
                return self.x - 1, self.y
            case Direction.E:
                return self.x + 1, self.y

    def moveForward(self):
        match self.direction:
            case Direction.N:
                self.y = self.y - 1
            case Direction.S:
                self.y = self.y + 1
            case Direction.W:
                self.x = self.x - 1
            case Direction.E:
                self.x = self.x + 1

    def isOutOfBound(self, area_map):
        if self.y < 0 or self.x < 0 or self.y >= len(area_map) or self.x >= len(area_map[0]):
            return True

        return False


def main():
    filename = "input.txt"
    area_map = []

    with open(filename) as file:
        for line in file:
            area_map.append(line)

    print("====== MAP START ======")
    for row in area_map:
        print(row)

    print("====== MAP END ======")

    print("Part 1 answer:")
    part1_find_path(area_map.copy())

    print("Part 2 answer:")
    for row in area_map:
        print(row)
    part2_find_loops(area_map.copy())


def part1_find_path(area_map: list[str]):
    x, y, dir = getStartingPosAndDirection(area_map)

    print("Initial position of guard:")
    print(f"{x=}, {y=}")
    print(f"{dir=}")

    guard = Guard(x, y, dir)

    while(not guard.isOutOfBound(area_map)):
        guard.nextMove(area_map)

    # Count number of individual spaces navigated by the guard (also trace the route into a file, because it's kinda neat)
    cnt = 0
    with open('output_part1.txt', 'w') as file:
        for row in area_map:
            cnt = cnt + row.count("X")
            file.write(row)

    print(cnt)

def part2_find_loops(area_map: list[str]):
    x, y, dir = getStartingPosAndDirection(area_map)

    guard = Guard(x, y, dir, area_map)

    while(not guard.isOutOfBound(area_map)):
        guard.nextMove(area_map)

    with open('output_part2.txt', 'w') as file:
        for row in area_map:
            file.write(row)

    print(guard.nb_loops)

def getStartingPosAndDirection(area_map):

    for y, row in enumerate(area_map):
        for dir_char in ["^", ">", "v", "<"]:
            if dir_char in row:
                match dir_char:
                    case "^":
                        return (row.find(dir_char), y, Direction.N)
                    case ">":
                        return (row.find(dir_char), y, Direction.E)
                    case "v":
                        return (row.find(dir_char), y, Direction.S)
                    case "<":
                        return (row.find(dir_char), y, Direction.W)
    return -1, -1, Direction.N

if __name__ == "__main__":
    main()
    #test_part1_getTotalMiddleValues()
    #test_part2_getTotalMiddleValues()
