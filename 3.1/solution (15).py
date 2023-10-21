L = int(input())
N = int(input())
all_strr = []
for _ in range(N):
    strr = input()
    all_strr.append(strr)

ostL = L - 3
count = 1
for strr in all_strr:
    if ostL == 0:
        break
    elif len(strr) >= ostL:
        print(f"{strr[0:ostL]}...")
        break
    else:
        print(strr)
        ostL = ostL - len(strr)
    count += 1