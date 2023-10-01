n = int(input())
c = 0
for i in range(n):
    ns = ""
    while (j := input()) != "ВСЁ":
        ns += j
    if "зайка" in ns:
        c += 1
print(c)
