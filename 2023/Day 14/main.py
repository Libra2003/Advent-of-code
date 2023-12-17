def roll_north():
    dirty = True
    while dirty:
        dirty = False
        for y, line in enumerate(grid[:-1]):
            for x, space in enumerate(line):
                if space == '.' and grid[y + 1][x] == 'O':
                    line[x] = 'O'
                    grid[y + 1][x] = '.'
                    dirty = True

def roll_south():
    dirty = True
    while dirty:
        dirty = False
        for y, line in enumerate(grid[1:]):
            for x, space in enumerate(line):
                if space == '.' and grid[y][x] == 'O':
                    line[x] = 'O'
                    grid[y][x] = '.'
                    dirty = True

def roll_east():
    dirty = True
    while dirty:
        dirty = False
        for line in grid:
            l = ''.join(line)
            if 'O.' in l:
                line[:] = l.replace('O.', '.O')
                dirty = True

def roll_west():
    dirty = True
    while dirty:
        dirty = False
        for line in grid:
            l = ''.join(line)
            if '.O' in l:
                line[:] = l.replace('.O', 'O.')
                dirty = True

def weigh():
    weight = 0
    for y, line in enumerate(grid[::-1]):
        weight += (y + 1) * line.count('O')

    print(weight)

grid = [list(l) for l in open('input.txt').read().split()]
roll_north()
weigh()

grid = [list(l) for l in open('input.txt').read().split()]
hashes = []
target = 0

while True:
    h = hash(tuple([''.join(l) for l in grid]))
    if not target and h in hashes:
        start = hashes.index(h)
        length = len(hashes) - start
        target = (1000000000 - start) % length + start + length

    if len(hashes) == target and target:
        break

    hashes.append(h)
    roll_north()
    roll_west()
    roll_south()
    roll_east()

weigh()