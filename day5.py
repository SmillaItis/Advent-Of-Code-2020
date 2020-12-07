
with open(r'tickets.txt', 'r') as f:
    text = f.readlines()


def solve(s):
    min1 = 0
    max1 = 128

    for i in range(7):
        c = s[i]
        if c == "F":
            max1 = max1 - (max1-min1)/2
        elif c == "B":
            min1 = min1 + (max1 - min1)/2
    return min1


def solveright(s):
    min1 = 0
    max1 = 8

    for i in range(7, 10):
        c = s[i]
        if c == "L":
            max1 = max1 - (max1-min1)/2
        elif c == "R":
            min1 = min1 + (max1 - min1)/2
    return min1


nums = []


def output():
    for s in text:
        r = solve(s)
        seat = solveright(s)
        y = r*8 + seat
        nums.append(int(y))


output()
t = nums.sort()
res = [ele for ele in range(max(nums)) if ele not in nums]
print(str(res))
