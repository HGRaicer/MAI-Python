n = input()
flag = True
for i in range(len(n)):
    if n[i] != n[len(n) - 1 - i]:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
