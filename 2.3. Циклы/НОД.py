a = int(input())
b = int(input())
flag = True
while flag:
    ost = a % b
    if ost == 0:
        print(b)
        flag = False
    else:
        a = b
        b = ost
