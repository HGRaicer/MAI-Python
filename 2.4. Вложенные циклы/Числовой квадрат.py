n = int(input())
k = len(str((n + 1) // 2))

for i in range(1, (n + 1) // 2 + 1):
    for j in range(1, (n + 1) // 2 + 1):
        print(f"{min(i, j):>{k}}", end=" ")
    for j in range(n // 2, 0, -1):
        print(f"{min(i, j):>{k}}", end=" ")
    print()
for i in range(n // 2, 0, -1):
    for j in range(1, (n + 1) // 2 + 1):
        print(f"{min(i, j):>{k}}", end=" ")
    for j in range(n // 2, 0, -1):
        print(f"{min(i, j):>{k}}", end=" ")
    print()


