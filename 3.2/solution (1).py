set_ = set()
ans = []
strr = input()
strr2 = input()
for symb in strr:
    set_.add(symb)

for symb in strr2:
    if symb in set_:
        if symb not in ans:
            ans.append(symb)
            print(symb, end="")
