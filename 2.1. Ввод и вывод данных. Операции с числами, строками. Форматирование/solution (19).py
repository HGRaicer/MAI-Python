n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
for i in range(1, n + 1):
    j = n - i
    if (i * k1 + j * k2) // n == m:
        print(i, j)
        break
