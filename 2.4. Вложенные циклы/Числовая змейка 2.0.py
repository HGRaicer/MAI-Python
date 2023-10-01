n = int(input())
m = int(input())
le = n * m
le = str(le)
le = len(le)
mas = [0] * n
for z in range(n):
    mas[z] = [0] * m
for i in range(1, m + 1):
    k = 0
    if i % 2 != 0:
        for j in range(n * (i - 1) + 1, n * i + 1):
            mas[k][i - 1] = f"{j:>{le}}"
            k += 1
    else:
        for j in range(n * i, n * (i - 1), -1):
            mas[k][i - 1] = f"{j:>{le}}"
            k += 1
for i in range(len(mas)):
    print(*mas[i], end="\n")
