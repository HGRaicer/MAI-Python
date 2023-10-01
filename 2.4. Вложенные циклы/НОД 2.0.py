n = int(input())
a = int(input())
ans = 0
for i in range(n - 1):
    b = int(input())
    flag = True
    while flag:
        ost = a % b
        if ost == 0:
            ans = b
            flag = False
            a = b
        else:
            a = b
            b = ost
print(ans)
