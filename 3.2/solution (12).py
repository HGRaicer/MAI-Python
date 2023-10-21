N = int(input())

porridge = [input() for _ in range(N)]
set_por = set()
M = int(input())
for _ in range(M):
    for _ in range(int(input())):
        set_por.add(input())

porridge.sort()
flag = True
for por in porridge:
    if por in set_por:
        pass
    else:
        flag = False
        print(por)
if flag:
    print("Готовить нечего")
