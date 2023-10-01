leng = []
for i in range(3):
    leng.append(int(input()))

if (
    leng[0] + leng[1] > leng[2]
    and leng[1] + leng[2] > leng[0]
    and leng[0] + leng[2] > leng[1]
):
    print("YES")
else:
    print("NO")
