def main():
    filename = "input.txt"
    reports: list[list[int]] = []

    with open(filename) as file:
        for line in file:
            report = [int(level) for level in line.split()]

            reports.append(report)

    print("Part 1 answer:")
    part1_getSafeReportAmount(reports)

    print("Part 2 answer:")
    part2_getSafeReportAmount(reports)

def part1_getSafeReportAmount(reports: list[list[int]]):
    nb_safe_reports = 0

    for report in reports:
        if not is_failed_report(report) :
            nb_safe_reports = nb_safe_reports + 1

    print(nb_safe_reports)

def part2_getSafeReportAmount(reports: list[list[int]]):
    nb_safe_reports = 0

    for report in reports:
        failed = is_failed_report(report)

        if not failed:
            nb_safe_reports = nb_safe_reports + 1
            continue

        if failed:
            # Just go horse each possibility until I tried them 'em all, or found a winner
            for i, _ in enumerate(report):
                report_copy = report.copy()
                report_copy.pop(i)
                failed = is_failed_report(report_copy)

                if not failed:
                    nb_safe_reports = nb_safe_reports + 1
                    break

    print(nb_safe_reports)

def is_failed_report(report: list[int]):
    ascending = True
    failed = False

    for index, cur_level in enumerate(report):
        if index == 0 :
            continue

        if index == 1 :
            ascending = (cur_level - report[index - 1]) > 0

        diff = cur_level - report[index - 1]
        if diff == 0 or abs(diff) > 3 or (ascending and diff < 0) or (not ascending and diff > 0) : 
            failed = True
            break

    return failed
        
def test_part1_getSafeReportAmount():
    reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [1, 3, 6, 7, 9],
            [1, 3, 2, 4, 5],
            [5, 9, 4, 3, 2]
    ]
    part1_getSafeReportAmount(reports)

def test_part2_getSafeReportAmount():
    reports = [
            [7, 6, 4, 2, 1], # Good descending
            [1, 3, 6, 7, 9], # Good ascending
            [7, 3, 4, 2, 1], # Good descending if 3 is removed
            [7, 3, 3, 2, 1], # Good descending if 3 is removed
            [7, 3, 8, 2, 1], # Bad descending (because of 7 to 3 and 8 to 2)
            [1, 2, 7, 8, 9], # Bad with too high jump at index != 0 and 1
            [1, 7, 8, 9, 10], # Bad with too high jump at index = 1
            [1, 3, 2, 4, 5], # Good if 3 is removed
            [5, 9, 4, 3, 2], # Good if 9 is removed
            [5, 4, 9, 3, 2], # Good if 9 is removed
            [5, 4, 3, 4, 2], # Good if second 4 is removed
            [5, 9, 3, 4, 2], # Bad with multiple fails
            [83, 84, 87, 85, 86, 87] # Good if 87 is removed
    ]
    part2_getSafeReportAmount(reports)

if __name__ == "__main__":
    main()
    #test_part1_getSafeReportAmount()
    #test_part2_getSafeReportAmount()
