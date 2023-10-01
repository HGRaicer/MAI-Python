a = int(input())
b = int(input())
ma = max(a, b)
flag = True
while flag:
    if ma % a == 0 and ma % b == 0:
        print(ma)
        flag = False
    ma += 1
