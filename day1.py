f = open(r'done\advent\input.txt', "r")
mylist = []
for line in f:
    mylist.append(int(line.strip('\n')))
for x in mylist:
    for y in mylist:
        for z in mylist:
            sumnum = x + y + z
            if sumnum == 2020:
                print(x*y*z)
