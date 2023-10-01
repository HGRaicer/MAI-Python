chislo = input()
k = []
for i in range(len(chislo)):
    k.append(int(chislo[i]))
k.sort()
print(k[-1])
