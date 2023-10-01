n = input()
k = [int(i) for i in n]
ma = max(k)
mi = min(k)
if (ma + mi) == 2 * (sum(k) - mi - ma):
    print("YES")
else:
    print("NO")

