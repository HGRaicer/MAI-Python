n = int(input())
m = int(input())
le = n * m
le = str(le)
le = len(le)
k = 0
for i in range(n):
    for j in range(m):
        print(f"{((i+1)+n*j):>{le}}", end=" ")
    print()
