names = dict()
N = int(input())

for i in range(N):
    name = input()
    try:
        names[name] += 1
    except KeyError:
        names[name] = 1
flag = True
for i in sorted(names):
    if names[i] > 1:
        print(i, "-", names[i])
        flag = False

if flag:
    print("Однофамильцев нет")
