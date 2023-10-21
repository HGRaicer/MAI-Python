n = int(input())
flag = True
for _ in range(n):
    strr = input()
    if not (strr[0] in ["а", "б", "в"]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")
