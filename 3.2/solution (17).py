trush = []
count = []
N = int(input())
for _ in range(N):
    txy = tuple(map(lambda x: x // 10, map(int, input().split())))
    if txy in trush:
        count[trush.index(txy)] += 1
    else:
        trush.append(txy)
        count.append(1)

print(max(count))
