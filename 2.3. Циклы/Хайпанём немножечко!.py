n = int(input())
h1 = 0
flag = False
for i in range(n):
    flag = False
    b = int(input())
    for r in range(256):
        for m in range(256):
            h = (37 * (m + r + h1)) % 256
            if h < 100:
                if b == h + r * 256 + m * 256 ** 2:
                    h1 = h
                    flag = True

            if flag:
                break
        if flag:
            break
    if not flag:
        print(i)
        break

if flag:
    print("-1")