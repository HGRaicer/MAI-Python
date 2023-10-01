n = int(input())
m = int(input())
le = n * m
le = str(le)
le = len(le)
k = 0
for _ in range(n):
    for _ in range(m):
        k += 1
        print(f"{k:>{le}}", end=" ")
    print()
