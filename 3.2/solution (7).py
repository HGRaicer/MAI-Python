N = int(input())
count = 0
L1 = []
for _ in range(N):
    strr = tuple(input().split())
    L1.append(strr)
porridge = input()
L1.sort()
count = 0
for elem in L1:
    for por in elem:
        if por == porridge:
            count += 1
            print(elem[0])
if count == 0:
    print("Таких нет")