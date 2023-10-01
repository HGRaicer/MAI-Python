n = int(input())
i = 1
st = 0
flag = True
while flag:
    for j in range(i):
        st += 1
        print(st, end=' ')
        if st == n:
            flag = False
            break

    i += 1
    print()
