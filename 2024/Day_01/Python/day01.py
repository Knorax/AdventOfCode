
def main():
    filename = "input.txt"
    left_coords = []
    right_coords = []

    with open(filename) as file:
        for line in file:
            left, right = line.split(None, 1)

            left_coords.append(int(left))
            right_coords.append(int(right))

    # Run both part 1 and part 2 of the AoC solution
    part1_get_diff(left_coords, right_coords)
    part2_get_similarity(left_coords, right_coords)

# Gets the sum of the differences between the two sorted coordinate list
def part1_get_diff(left_coords, right_coords):
    left_coords.sort()
    right_coords.sort()
    sum = 0

    for _, (left_val, right_val) in enumerate(zip(left_coords, right_coords)):
        sum = sum + abs(left_val - right_val)

    print(f"Part 1 difference: {sum}")

# Gets the similarity score between both coordinate lists
def part2_get_similarity(left_coords, right_coords):
    score = 0

    for left_val in left_coords:
        nb_duplicate = right_coords.count(left_val)
        score = score + left_val * nb_duplicate

    print(f"Part 2 similarity score: {score}")

# Rough test function for part 1
def test_get_diff():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]

    part1_get_diff(left, right)

# Rough test function for part 2
def test_get_similarity():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]

    part2_get_similarity(left, right)

if __name__ == "__main__":
    main()
    #test_get_diff()
    #test_get_similarity()
