

class PageRule:
    def __init__(self):
        # List of pages that needs to be after the current page
        self.next_pages = []

    def add_next_page(self, page_nb):
        self.next_pages.append(page_nb)

    # Checks if a page number is in the rules of this page 
    def has_rule_for_page(self, page_nb):
        return page_nb in self.next_pages

    def __repr__(self) -> str:
        return ", ".join(map(str, self.next_pages))
    
def main():
    filename = "input.txt"
    rules = [PageRule() for _ in range(100)]
    updates = [] 

    with open(filename) as file:
        for line in file:
            if "|" in line:
                left, right = line.split("|")
                left = int(left)
                right = int(right)
                rules[left].add_next_page(right)

            elif len(line) > 1:
                update = line.split(",")
                update = [int(x) for x in update]
                updates.append(update)

    for i, rule in enumerate(rules):
        print(f"{i} : {rule}")
    print("Part 1 answer:")
    bad_updates = part1_getTotalMiddleValues(rules, updates)

    print("Part 2 answer:")
    part2_getTotalBadUpdateMiddleValues(rules, bad_updates)

def part1_getTotalMiddleValues(rules: list[PageRule], updates: list[list[int]]):
    # Go through each update list
        # For each page (starting from second element)
            # Go through each element before this page in the list
                # Check if this element is in this page's rule list
                # If it is, the element should be after this element, so that's a bady
                # If it's not, the element doesn't have to be after, so we good 
            # They were all good? 
            # Yes, we take the middle number
            # No? We ignore that boi
    middle_elements = []
    bad_updates = []
    for update in updates:
        valid_update = True

        for i, page_nb in enumerate(update[1:]):
            for _, prev_page in enumerate(update[:i+1]):
                if rules[page_nb].has_rule_for_page(prev_page):
                    valid_update = False
                    bad_updates.append(update)
                    break
            if not valid_update:
                break # We don't have to pass through the subsequent checks for this update

        if valid_update:
            middle_elements.append(update[int(len(update) / 2)])

    
    print(sum(middle_elements))
    return bad_updates

def part2_getTotalBadUpdateMiddleValues(rules: list[PageRule], updates: list[list[int]]):
    middle_elements = []

    # Same kind of navigation as part 1, but we do a swap on the values when we break a rule
    for update in updates:
        for i, _ in enumerate(update[1:]):
            for j, _ in enumerate(update[:i+1]):
                if rules[update[i+1]].has_rule_for_page(update[j]):
                    # Swap the values
                    temp = update[i+1]
                    update[i+1] = update[j]
                    update[j] = temp 

        middle_elements.append(update[int(len(update) / 2)])
    
    print(sum(middle_elements))

def test_part1_getTotalMiddleValues():
    rules = [PageRule() for _ in range(10)]
    updates = [
        [1, 2, 3, 4, 5], # Good update : 3
        [3, 2, 1], # Bad update
        [4, 2, 5], # good update : 2
        [5, 2, 4, 3, 9], # Bad update
        [4, 2, 5, 3, 7], # good update : 5
    ] # Total should be 10

    rules[1].add_next_page(3)
    rules[1].add_next_page(4)

    rules[2].add_next_page(3)

    rules[4].add_next_page(5)

    part1_getTotalMiddleValues(rules, updates)


def test_part2_getTotalMiddleValues():
    rules = [PageRule() for _ in range(10)]
    updates = [
        [2, 1, 3, 5, 4],
        [2, 1, 5, 3, 4],
        [2, 1, 5, 4, 3],
        [5, 2, 4, 3, 9], # Bad update
        [94, 68, 73, 78, 15, 65, 43, 66, 62],
    ] # Total should be 10

    rules[1].add_next_page(2)
    rules[1].add_next_page(3)

    rules[2].add_next_page(3)

    rules[4].add_next_page(5)

    for i, rule in enumerate(rules):
        print(f"{i} : {rule}")

    part2_getTotalBadUpdateMiddleValues(rules, updates)

if __name__ == "__main__":
    main()
    #test_part1_getTotalMiddleValues()
    #test_part2_getTotalMiddleValues()
