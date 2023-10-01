s1 = input()
s2 = input()
s3 = input()
k = [s1, s2, s3]
k.sort()
for i in range(3):
    if "зайка" in k[i]:
        print(k[i], len(k[i]))
        break
