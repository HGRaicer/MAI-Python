N = int(input())
all_strr = []
for _ in range(N):
    strr = input()
    all_strr.append(strr)
finds = input()

for strr in all_strr:
    if finds.lower() in strr.lower():
        print(strr)
