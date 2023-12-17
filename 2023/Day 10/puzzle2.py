def main():
    g = [list(line.strip("\n")) for line in open("input.txt", "r").readlines()]

    for i in range(len(g)):
        g[i].append(".")
        g[i].insert(0, ".")

    g.append(list("." * len(g[0])))
    g.insert(0, list("." * len(g[0])))

    t = [".", "-", "|", "7", "J", "L", "F"]

    to = [
        [-1, -1, 0, 3, -1, -1, 1],
        [-1, 1, -1, 2, 0, -1, -1],
        [-1, -1, 2, -1, 3, 1, -1],
        [-1, 3, -1, -1, -1, 0, 2],
    ]

    def fl(p, d, a):
        init = p.copy()

        while True:
            a(tuple(p), d)
            p = gn(p, d)
            a(tuple(p), d)

            if p == init:
                break

            d = to[d][t.index(g[p[1]][p[0]])]

    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == "S":
                p = [j, i]
                break

    d = []
    if to[0][t.index(g[p[1] - 1][p[0]])] != -1:
        d.append(0)
    if to[1][t.index(g[p[1]][p[0] + 1])] != -1:
        d.append(1)
    if to[2][t.index(g[p[1] + 1][p[0]])] != -1:
        d.append(2)
    if to[3][t.index(g[p[1]][p[0] - 1])] != -1:
        d.append(3)

    d.sort()

    match d:
        case [0, 1]:
            s_t = "L"
        case [0, 2]:
            s_t = "|"
        case [0, 3]:
            s_t = "J"
        case [1, 2]:
            s_t = "F"
        case [1, 3]:
            s_t = "-"
        case [2, 3]:
            s_t = "7"

    g[p[1]][p[0]] = s_t

    lt = set()
    fl(p, d[0], lambda t, d: lt.add(t))

    p = sorted(lt, key=lambda t: (t[-1], t[0]))[0]
    d = 1

    it = set()

    def mi(p, d):
        id = (d + 1) % 4
        itp = gn(p, id)

        if tuple(itp) not in lt:
            it.add(tuple(itp))

    fl(list(p), d, mi)

    for i in range(1, len(g) - 1):
        for j in range(1, len(g[i]) - 1):
            if (i, j) not in lt and (i, j) not in it:
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if (k, l) in it:
                            it.add((i, j))

    print(len(it))


def gn(p, d):
    match d:
        case 0:
            p = [p[0], p[1] - 1]
        case 1:
            p = [p[0] + 1, p[1]]
        case 2:
            p = [p[0], p[1] + 1]
        case 3:
            p = [p[0] - 1, p[1]]

    return p


if __name__ == "__main__":
    main()
