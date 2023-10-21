stop = True
all_str = ""
while stop:
    strr = input()
    if strr == "ФИНИШ":
        stop = False
    else:
        all_str += strr.lower()
alf = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ё",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ь",
    "ю",
    "я",
]
alfcolv = []
for ch in alf:
    alfcolv.append(all_str.count(ch))
ma = 0
idx = 0
for i in range(len(alf)):
    if alfcolv[i] > ma:
        ma = alfcolv[i]
        idx = i
print(alf[idx])
