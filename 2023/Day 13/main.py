data = open('input.txt').read().strip().split('\n\n')

def alter_pattern(pattern):
    return list(map(list, zip(*pattern)))

def discover_mirror(pattern, nonmatches):
    pattern = ["".join(x) for x in pattern]
    for i in range(len(pattern) - 1):
        mismatches_count = 0
        for j in range(len(pattern)):
            if i + 1 + (i - j) in range(len(pattern)) and pattern[j] != pattern[i + 1 + (i - j)]:
                mismatches_count += len([k for k in range(len(pattern[j])) if pattern[j][k] != pattern[i + 1 + (i - j)][k]])
        if mismatches_count == nonmatches:
            return i
    return None

def analyze_pattern(pattern, nonmatches):
    pattern = [list(x) for x in pattern.split('\n')]
    row = discover_mirror(pattern, nonmatches)
    if row is not None:
        return 100 * (row + 1)
    col = discover_mirror(alter_pattern(pattern), nonmatches)
    if col is not None:
        return (col + 1)

result_part_1 = 0
result_part_2 = 0
for i, line in enumerate(data):
    result_part_1 += analyze_pattern(line, 0)
    result_part_2 += analyze_pattern(line, 2)

print(result_part_1, result_part_2)
