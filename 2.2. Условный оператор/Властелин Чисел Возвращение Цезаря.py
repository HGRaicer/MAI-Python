leng = []
strn = input()
strn2 = input()
for i in range(2):
    leng.append(int(strn[i]))
    leng.append(int(strn2[i]))
leng.sort()
print(f"{leng[-1]}{(leng[-2]+leng[-3])%10}{leng[0]}")
