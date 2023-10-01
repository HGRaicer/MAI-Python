n = int(input())
s = 0
for _ in range(n):
    ch = input()
    if ch == ch[::-1]:
        s += 1
print(s)
