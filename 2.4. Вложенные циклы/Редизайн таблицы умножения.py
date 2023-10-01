n = int(input())
m = int(input())
s = ""
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s += f"{i * j :^{m}}"
        if j != n:
            s += '|'
    if i != n:
        s += f"\n{'-' * (n * m + (n - 1))}\n"
print(s)
