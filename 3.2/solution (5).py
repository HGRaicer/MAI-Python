D1 = dict()
N = int(input())
M = int(input())
count = N + M
for _ in range(N + M):
    strr = input()
    try:
        D1[strr] += 1
    except KeyError:
        D1[strr] = 1

keyd1 = list(D1.keys())
keyd1.sort()
count = 0
for i in keyd1:
    if D1[i] == 1:
        count += 1
        print(i)
if count == 0:
    print("Таких нет")
