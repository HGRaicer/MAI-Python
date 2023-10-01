n = int(input())
m = int(input())
le = n * m
le = str(le)
le = len(le)
k = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(m * (i - 1) + 1, m * i + 1):
            print(f"{j:>{le}}", end=" ")
        print()
    else:
        for j in range(m * i, m * (i - 1), -1):
            print(f"{j:>{le}}", end=" ")
        print()