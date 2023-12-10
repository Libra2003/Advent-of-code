file_handle = open("input.txt", "r")
lines = file_handle.readlines()
result_sum = 0

conversion_dict = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    "zero": "z0o"
}

for line in lines:
    first_digit = None
    last_digit = None
    translated_line = line

    for key, value in conversion_dict.items():
        translated_line = translated_line.replace(key, value)

    for character in translated_line:
        if character.isdigit() and first_digit is None:
            first_digit = character
            last_digit = character
        elif character.isdigit():
            last_digit = character

    if first_digit is not None and last_digit is not None:
        joined_digits = first_digit + last_digit
        result_sum += int(joined_digits)

file_handle.close()
print(result_sum)
