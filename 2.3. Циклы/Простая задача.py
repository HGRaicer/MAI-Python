chislo = int(input())

flag = False
for i in range(2, int(chislo ** 0.5 + 1)):
    if chislo % i == 0:
        flag = False
        break
    else:
        flag = True

if flag:
    print("YES")
else:
    print("NO")
