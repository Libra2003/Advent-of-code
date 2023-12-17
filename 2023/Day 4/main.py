import re


def calculate_score_from_line(line):
    match_result = re.match(r"Card\s+(\d+):\s+(.*?)\s\|\s+(.*?)$", line)
    winning_cards = set(int(num) for num in match_result.group(2).strip().split())
    card_numbers = set(int(num) for num in match_result.group(3).strip().split())
    return winning_cards.intersection(card_numbers)


total_score_part1 = 0
input_lines = open("input.txt").read().strip().splitlines()
total_score_part2 = [1] * len(input_lines)

for index, input_line in enumerate(input_lines):
    matches_result = calculate_score_from_line(input_line)
    total_score_part1 += int(2 ** (len(matches_result) - 1))
    for i in range(len(matches_result)):
        total_score_part2[index + i + 1] += total_score_part2[index]

print(f"Result for Part One: {total_score_part1}")
print(f"Result for Part Two: {sum(total_score_part2)}")

