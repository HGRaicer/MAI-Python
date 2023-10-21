around = set()
while (strr := input()) != "":
    listrr = strr.split()
    for idx in range(len(listrr)):
        if listrr[idx] == "зайка":
            if idx > 0:
                around.add(listrr[idx - 1])
            if idx < len(listrr) - 1:
                around.add(listrr[idx + 1])
for elev in around:
    print(elev)
