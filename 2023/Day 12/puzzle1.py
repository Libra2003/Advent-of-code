f = open("input.txt")
s = 0

def matches(txt, nums):
    st = "."
    for n in nums:
        for i in range(int(n)):
            st += "#"
        st += "."

    st_dict = {0: 1}
    new_dict = {}
    for c in txt:
        for state in st_dict:
            if c == "?":
                if state + 1 < len(st):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + st_dict[state]
                if st[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + st_dict[state]
            elif c == ".":
                if state + 1 < len(st) and st[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + st_dict[state]
                if st[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + st_dict[state]
            elif c == "#":
                if state + 1 < len(st) and st[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + st_dict[state]

        st_dict = new_dict
        new_dict = {}

    return st_dict.get(len(st) - 1, 0) + st_dict.get(len(st) - 2, 0)

for line in f.readlines():
    line = line.strip().split(" ")
    txt = line[0]
    nums = line[1].split(",")

    s += matches(txt, nums)

print(s)
