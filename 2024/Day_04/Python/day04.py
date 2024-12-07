
from enum import Enum


class Direction(Enum):
    W = 0
    NW = 1
    N = 2
    NE = 3
    E = 4
    SE = 5
    S = 6
    SW = 7 

MAS = "MAS"
    
def main():
    filename = "input.txt"
    data = [] 

    with open(filename) as file:
        for line in file:
            data.append(line)

    print(data)
    print("Part 1 answer:")
    part1_findXMAS(data)

    print("Part 2 answer:")
    part2_findCrossMAS(data)

def part1_findXMAS(data: list[str]):
    nb_found = 0
    # Search for a X
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if data[i][j] == 'X':
                # Scatter search around this point
                nb_found = nb_found + scatterSearch(data, MAS, j, i)

    print(nb_found)

def part2_findCrossMAS(data: list[str]):
    nb_found = 0
    # Search for a A
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if data[i][j] == 'A':
                # Scatter "X" search around this point
                m_found, m_dirs = scatterXSearch(data, "M", j, i)
                s_found, s_dirs = scatterXSearch(data, "S", j, i)
                
                if m_found != 2 or s_found != 2:
                    continue

                cnt = 0
                for m_dir in m_dirs:
                    cnt = cnt + 1 if areOppositeDirection(m_dir, s_dirs[0]) else cnt
                    cnt = cnt + 1 if areOppositeDirection(m_dir, s_dirs[1]) else cnt

                if cnt == 2:
                    nb_found = nb_found + 1

    print(nb_found)

# Search word in a cross pattern 
def scatterXSearch(data, word, x, y):
    nb_found = 0
    dir_found = []
    for dir in [Direction.SW, Direction.NW, Direction.NE, Direction.SE]:
        if searchStrInDirection(data, word, x, y, dir):
            nb_found = nb_found + 1
            dir_found.append(dir)

    return nb_found, dir_found

# Search word in a snow flake pattern (very thematic)
def scatterSearch(data, word, x, y):
    nb_found = 0
    for dir in Direction:
        nb_found = nb_found + 1 if searchStrInDirection(data, word, x, y, dir) else nb_found

    return nb_found

# Recursively check in the set direction if all the char in the char_queue sequence are present in order
def searchStrInDirection(data, word, cur_x, cur_y, dir: Direction):

    next_x = cur_x
    next_y = cur_y

    # If we were able to empty the queue, it means we found the whole character sequence!
    if len(word) == 0:
        return True

    next_x = getNextX(cur_x, dir)
    next_y = getNextY(cur_y, dir)

    # If we are no longer in the data's boundaries, we didn't find the word
    if next_x < 0 or next_y < 0 or next_x >= len(data[0]) or next_y >= len(data):
        return False

    to_find = word[0]
    if data[next_y][next_x] != to_find:
        return False

    word = word[1:]
    # Go to the next character in the same direction (with one less character in the queue)
    return searchStrInDirection(data, word, next_x, next_y, dir)

def getNextY(cur_y, dir: Direction):
    if dir in [Direction.SW, Direction.S, Direction.SE]:
        return cur_y + 1
    elif dir in [Direction.NW, Direction.N, Direction.NE]:
        return cur_y - 1

    return cur_y

def getNextX(cur_x, dir: Direction):
    if dir in [Direction.SW, Direction.W, Direction.NW]:
        return cur_x - 1
    elif dir in [Direction.SE, Direction.E, Direction.NE]:
        return cur_x + 1

    return cur_x

def areOppositeDirection(dir1: Direction, dir2: Direction):
    if (dir1.value + 4) % 8 == dir2.value:
        return True
    return False

# Test caseses for string search
def test_searchStrInDirection():
    word = "23"
    data = [
        "33333",
        "22222",
        "32123",
        "22222",
        "32333",
        "11111",
    ]

    assert searchStrInDirection(data, word, 2, 2, Direction.N) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.NE) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.E) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.SE) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.S) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.SW) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.W) == True
    assert searchStrInDirection(data, word, 2, 2, Direction.NW) == True

    assert searchStrInDirection(data, word, 0, 5, Direction.W) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.NW) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.N) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.NE) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.E) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.SE) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.S) == False 
    assert searchStrInDirection(data, word, 0, 5, Direction.SW) == False 


def test_part1():
    data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
    ]
    part1_findXMAS(data)

    print(scatterSearch(data, MAS, 4, 0))
    print(scatterSearch(data, MAS, 5, 0))

    print(scatterSearch(data, MAS, 4, 1))

    print(scatterSearch(data, MAS, 9, 3))

    print(scatterSearch(data, MAS, 0, 4))
    print(scatterSearch(data, MAS, 6, 4))
    
    print(scatterSearch(data, MAS, 0, 5))
    print(scatterSearch(data, MAS, 6, 5))

    print(scatterSearch(data, MAS, 1, 9))
    print(scatterSearch(data, MAS, 3, 9))
    print(scatterSearch(data, MAS, 5, 9))
    print(scatterSearch(data, MAS, 9, 9))

if __name__ == "__main__":
    main()
    #test_part1()
    #test_searchStrInDirection()
    #test_part1_getMultiplificationCommands()
    #test_part2_getMultiplyCommandWithEnables()
