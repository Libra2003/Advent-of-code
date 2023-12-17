from itertools import combinations

with open('input.txt', 'r') as f:
    pi = f.read()


def part1(pi):
    g = [[e for e in line] for line in pi.split('\n')]
    m, n = len(g), len(g[0])

    i = 0
    while i < len(g):
        if '#' not in g[i]:
            g.insert(i, ['.'] * n)
            m += 1
            i += 2
        else:
            i += 1

    j = 0
    while j < len(g[0]):
        if '#' not in [g[i][j] for i in range(m)]:
            for i in range(m):
                g[i].insert(j, '.')
            n += 1
            j += 2
        else:
            j += 1

    galaxies = [(i, j) for i in range(m) for j in range(n) if g[i][j] == '#']
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        total += abs(x1 - x2) + abs(y1 - y2)

    return total


def part2(pi):
    g = [[e for e in line] for line in pi.split('\n')]
    m, n = len(g), len(g[0])

    empty_rows = [i for i in range(m) if '#' not in g[i]]
    empty_cols = [j for j in range(n) if all(g[i][j] == '.' for i in range(m))]
    galaxies = [(i, j) for i in range(m) for j in range(n) if g[i][j] == '#']

    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        add_rows = 999_999 * sum(r in range(x1, x2) for r in empty_rows)
        add_cols = 999_999 * sum(c in range(y1, y2) for c in empty_cols)
        total += x2 - x1 + add_rows + y2 - y1 + add_cols

    return total


print('Part 1:', part1(pi))
print('Part 2:', part2(pi))
