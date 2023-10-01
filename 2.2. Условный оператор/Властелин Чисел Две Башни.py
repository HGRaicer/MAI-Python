leng = []
strn = input()
for i in range(3):
    leng.append(int(strn[i]))
leng.sort()
if leng[0] == 0:
    k1 = leng[1]
    k2 = leng[0]
else:
    k1 = leng[0]
    k2 = leng[1]
print(f"{k1}{k2} {leng[2]}{leng[1]}")
