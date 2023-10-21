N = int(input())

rub = []
count = []
for _ in range(N):
    lstrr = input()
    lstrr = lstrr.replace(",", "")
    lstrr = lstrr.split()
    may = []
    for i in range(1, len(lstrr)):
        if lstrr[i] in rub and lstrr[i] not in may:
            count[rub.index(lstrr[i])] += 1
        elif lstrr[i] in rub and lstrr[i] in may:
            pass
        else:
            count.append(1)
            rub.append(lstrr[i])
            may.append(lstrr[i])

ans = []
for i in range(len(count)):
    if count[i] == 1:
        ans.append(rub[i])
ans.sort()
for el in ans:
    print(el)
