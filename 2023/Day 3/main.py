import re

data_lines = list(open('input.txt', 'r'))
result_part1 = 0
symbols_dict = {}
gears_dict = {}

for row_index in range(len(data_lines[0]) - 1):
    for col_index in range(len(data_lines)):
        if data_lines[row_index][col_index] not in '0123456789.':
            symbols_dict[(row_index, col_index)] = data_lines[row_index][col_index]
            if data_lines[row_index][col_index] == '*':
                gears_dict[(row_index, col_index)] = []

for row_num, row_data in enumerate(data_lines):
    for match in re.finditer(r'\d+', row_data):
        possibilities_list = []
        for i in range(match.start() - 1, match.end() + 1):
            possibilities_list.append((row_num - 1, i))
            possibilities_list.append((row_num, i))
            possibilities_list.append((row_num + 1, i))
        is_valid = False
        for possibility in possibilities_list:
            if possibility in symbols_dict:
                is_valid = True
                if possibility in gears_dict:
                    gears_dict[possibility].append(int(match.group()))
        if is_valid:
            result_part1 += int(match.group())
print('Result for Part One -', result_part1)
result_part2 = 0
for gear in gears_dict:
    if len(gears_dict[gear]) == 2:
        result_part2 += (gears_dict[gear][0] * gears_dict[gear][1])
print('Result for Part Two -', result_part2)