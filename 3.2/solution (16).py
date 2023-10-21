pairs = []
while (strr := input()) != "":
    pair = tuple(strr.split())
    pairs.append(pair)

pairsto2 = {}
pairs.sort()
onepep = set()
for pair in pairs:
    onepep.add(pair[0])
    onepep.add(pair[1])
onepep = list(onepep)
onepep.sort()
for elev in onepep:
    pairsto2[elev] = set()

for pair in pairs:
    osn = pair[0]
    frnd = pair[1]
    for elem in pairs:
        if elem[0] == frnd:
            if elem[1] != osn:
                pairsto2[osn].add(elem[1])
                pairsto2[elem[1]].add(osn)
        if elem[1] == frnd:
            if elem[0] != osn:
                pairsto2[osn].add(elem[0])
                pairsto2[elem[0]].add(osn)
        if elem[0] == osn:
            if elem[1] != frnd:
                pairsto2[frnd].add(elem[1])
                pairsto2[elem[1]].add(frnd)
        if elem[1] == osn:
            if elem[0] != frnd:
                pairsto2[frnd].add(elem[0])
                pairsto2[elem[0]].add(frnd)

for pair in pairs:
    if pair[1] in pairsto2[pair[0]]:
        pairsto2[pair[0]].remove(pair[1])
    if pair[0] in pairsto2[pair[1]]:
        pairsto2[pair[1]].remove(pair[0])

for key, value in pairsto2.items():
    val = list(value)
    val.sort()
    pairsto2[key] = val

for elev in pairsto2:
    print(elev, end=":")
    strr = ""
    for frnd in pairsto2[elev]:
        strr += f" {frnd},"
    print(strr[:-1])
