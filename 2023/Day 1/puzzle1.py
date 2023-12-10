file = open("input.txt")
res = 0

for line in file:
    first_Digit = None
    last_Digit = None
    joined = None


    for char in line:
        if char.isdigit() and first_Digit is None:
            first_Digit = char
            last_Digit = char
        elif char.isdigit():
            last_Digit = char
    if first_Digit is not None and last_Digit is not None:
        combined_digits = first_Digit+last_Digit
        res +=int(combined_digits)

print(res)