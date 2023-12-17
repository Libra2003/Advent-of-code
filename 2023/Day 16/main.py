import sys
sys.setrecursionlimit(1000000)

g = [list(x) for x in open('input.txt').read().strip().split('\n')]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
m = ['R', 'L', 'D', 'U']
mir = {
    '.': {'R': ['R'], 'L': ['L'], 'D': ['D'], 'U': ['U']},
    '-': {'R': ['R'], 'L': ['L'], 'D': ['L', 'R'], 'U': ['L', 'R']},
    '|': {'R': ['D', 'U'], 'L': ['D', 'U'], 'D': ['D'], 'U': ['U']},
    '/': {'R': ['U'], 'L': ['D'], 'D': ['L'], 'U': ['R']},
    '\\': {'R': ['D'], 'L': ['U'], 'D': ['R'], 'U': ['L']},
}

def c(s):
    i = set()
    def l(x, y, dr):
        if (x, y, dr) in i:
            return
        i.add((x, y, dr))
        mr = g[x][y]
        for nxt in mir[mr][dr]:
            nxt_dr = d[m.index(nxt)]
            nx = x + nxt_dr[0]
            ny = y + nxt_dr[1]
            if nx in range(len(g)) and ny in range(len(g[0])):
                l(nx, ny, nxt)
    l(s[0], s[1], s[2])
    return len(set([(x, y) for x, y, _ in i]))

tc = []
for x in range(len(g)):
    tc.append((x, 0, 'R'))
    tc.append((x, len(g[0]) - 1, 'L'))
for y in range(len(g[0])):
    tc.append((0, y, 'D'))
    tc.append((0, len(g) - 1, 'U'))

print(c((0, 0, 'R')))
print(max(c(test) for test in tc))
