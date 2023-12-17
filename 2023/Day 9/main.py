data_lines = open("input.txt").read().splitlines()

def calculate_value(sequence):
    if sequence[0] == sequence[1] == sequence[-1]:
        return sequence[-1]
    return sequence[-1] + calculate_value([sequence[i] - sequence[i - 1] for i in range(1, len(sequence))])

result_f1 = sum(calculate_value([int(element) for element in line.split()]) for line in data_lines)

def calculate_difference(sequence):
    if sequence[0] == sequence[1] == sequence[-1]:
        return sequence[0]
    return sequence[0] - calculate_difference([sequence[i] - sequence[i - 1] for i in range(1, len(sequence))])

result_f2 = sum(calculate_difference([int(element) for element in line.split()]) for line in data_lines)

print(result_f1)
print(result_f2)
