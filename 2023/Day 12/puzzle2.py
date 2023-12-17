f = open("input.txt")
s = 0

def matches(txt, nums):
    st = "."
    for nr in nums:
        for i in range(int(nr)):
            st += "#"
        st += "."

    st_dict = {0: 1}
    new_dict = {}
    for char in txt:
        for state in st_dict:
            if char == "?":
                if state + 1 < len(st):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + st_dict[state]
                if st[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + st_dict[state]
            elif char == ".":
                if state + 1 < len(st) and st[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + st_dict[state]
                if st[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + st_dict[state]
            elif char == "#":
                if state + 1 < len(st) and st[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + st_dict[state]

        st_dict = new_dict
        new_dict = {}

    return st_dict.get(len(st) - 1, 0) + st_dict.get(len(st) - 2, 0)

for line in f.readlines():
    line = line.strip().split(" ")
    txt = (5 * (line[0] + "?"))[:-1]
    nums = 5 * line[1].split(",")

    s += matches(txt, nums)

print(s)
