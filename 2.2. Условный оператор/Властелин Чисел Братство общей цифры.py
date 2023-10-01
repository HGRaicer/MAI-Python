leng = []
leng1 = []
for i in range(3):
    strn = input()
    leng1.append(int(strn[1]))
    leng.append(int(strn[0]))

if leng[0] == leng[1] == leng[2]:
    print(leng[0])
else:
    print(leng1[0])
