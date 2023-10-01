n = 1
s = 0
while n != 0:
    n = float(input())
    if n >= 500:
        s = s + n - 0.1 * n
    else:
        s += n
print(s)
