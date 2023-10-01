n = int(input())
ma = 0
for i in range(2, 11):
    an = n
    s = 0
    while an != 0:
        ost = an % i
        s += ost
        an = an // i
    if ma < s:
        ma = s
        mai = i

print(mai)
