n = int(input())
i = 1
st = 0
ss = ""
le = 0
flag = True
while flag:
    s = ''
    for j in range(i):
        st += 1
        s += str(st) + ' '
        if st == n:
            le = len(s[:-1])
            flag = False
            break
    ss += s[:-1] + '\n'
    i += 1
me = ss.split('\n')
for i in range(len(me) - 1):
    print(f"{me[i] :^{le}}")

