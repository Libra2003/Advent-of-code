from parse import parse

with open("input.txt") as f:
    ls = f.read().splitlines()

total = 0
for l in ls:
    game, rounds = parse("Game {:d}: {}", l)
    if all(
        (int(n) <= 12 if c == "red" else int(n) <= 13 if c == "green" else int(n) <= 14)
        for rs in rounds.split("; ")
        for n, c in (r.split(" ") for r in rs.split(", "))
    ):
        total += game
print(total)
