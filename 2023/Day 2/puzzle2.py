with open("input.txt") as f:
    ls = f.read().splitlines()

total = 0
for l in ls:
    m = {"red": 0, "green": 0, "blue": 0}
    rounds = l.split(": ")[1]
    for rs in rounds.split("; "):
        for r in rs.split(", "):
            n, c = r.split(" ")
            m[c] = max(m[c], int(n))
    total += m["red"] * m["green"] * m["blue"]
print(total)
