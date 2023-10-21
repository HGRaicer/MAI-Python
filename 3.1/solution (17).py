strr = input()
count = 1
for i in range(1, len(strr)):
    if strr[i] == strr[i - 1]:
        count += 1
        if i == len(strr) - 1:
            print(strr[i], count)
    else:
        print(strr[i - 1], count)
        count = 1
        if i == len(strr) - 1:
            print(strr[i], count)
