from itertools import groupby
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent
INPUT_PATH = Path(SCRIPT_PATH, "input.txt")


# INPUT_PATH = Path(SCRIPT_PATH, "inputs/example1.txt")

def parse_input(input_data):
    data_list = [line.split() for line in input_data.splitlines()]
    return data_list


def determine_hand_rank(hand, part2=False):
    if part2:
        joker_count = hand.count('J')
        hand = hand.replace('J', '')
    grouped_cards = sorted([list(g) for _, g in groupby(''.join(sorted(hand)))], key=len, reverse=True)
    if part2:
        for _ in range(joker_count):
            grouped_cards[0].append(grouped_cards[0][0])
    if len(set(hand)) == 2:
        return 5 if len(grouped_cards[0]) == 4 else 4
    else:
        return 3 if len(grouped_cards[0]) == 3 else 2


def sort_hands_by_rank(data, part2=False):
    hand_ranks = [[] for _ in range(7)]
    for hand in data:
        hand_rank = len(set(hand[0])) if not part2 else len(set(hand[0].replace('J', '')))
        if hand_rank <= 1:
            hand_ranks[6].append(hand)
        elif hand_rank in range(2, 4):
            hand_ranks[determine_hand_rank(hand[0], part2)].append(hand)
        else:
            hand_ranks[5 - hand_rank].append(hand)
    return hand_ranks


def print_hand_ranks(combined_list):
    for idx, hand in enumerate(combined_list):
        print(f"{hand[0]} was rank {idx + 1}")
        yield int(hand[1]) * (idx + 1)


def sort_power_and_combine(hand_ranks, order):
    sorted_power = [[] for _ in range(7)]
    for idx, hand_list in enumerate(hand_ranks):
        sorted_power[idx] = sorted(hand_list, key=lambda x: [order.index(c) for c in x[0] if c in order])
    combined_list = [[x, y] for nested_list in sorted_power for x, y in nested_list]
    return combined_list


def part1(parsed_data):
    hand_ranks = sort_hands_by_rank(parsed_data)
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    combined_list = sort_power_and_combine(hand_ranks, order)
    return sum(print_hand_ranks(combined_list))


def part2(parsed_data):
    hand_ranks = sort_hands_by_rank(parsed_data, True)
    order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    combined_list = sort_power_and_combine(hand_ranks, order)
    return sum(print_hand_ranks(combined_list))


if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        parsed_data = parse_input(f.read())

    print("--- PART 1 ---")
    answer1 = part1(parsed_data)

    print("\n--- PART 2 ---")
    answer2 = part2(parsed_data)

    print("\n--- ANSWERS ---")
    print(f"PART1 - The total winnings are {answer1}")
    print(f"PART2 - The total winnings are {answer2}")
