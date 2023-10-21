stop = True
while stop:
    strr = input()
    if strr == "":
        stop = False
    else:
        try:
            idx = strr.index("#")
            if idx != 0:
                print(strr[:idx])
            else:
                pass
        except ValueError:
            print(strr)
