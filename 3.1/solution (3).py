stop = True
while stop:
    strr = input()
    if strr == "":
        stop = False
    elif strr[0] == "#" and strr[1] == "#":
        if strr[-1:-4:-1] == "@@@":
            pass
        else:
            print(strr[2:])
    elif strr[-1:-4:-1] == "@@@":
        pass
    else:
        print(strr)
