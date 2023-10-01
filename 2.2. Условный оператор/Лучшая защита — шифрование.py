n = input()
k = int(n[-1]) + int(n[-2])
k1 = int(n[-3]) + int(n[-2])
if k > k1:
    print(f"{k}{k1}")
else:
    print(f"{k1}{k}")
