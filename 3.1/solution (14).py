numbs = list(map(int, input().split()))
ans = 0
a = numbs[0]
for i in range(1, len(numbs)):
    b = numbs[i]
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
