N = int(input())
if N == 0:
    print("Готовить нечего")
else:
    products = [input() for _ in range(N)]
    M = int(input())

    ans = []
    for _ in range(M):
        flag = True
        name = input()
        quantity = int(input())
        for _ in range(quantity):
            ingredient = input()
            if ingredient not in products:
                flag = False
        if flag:
            ans.append(name)

    if len(ans) == 0:
        print("Готовить нечего")
    else:
        ans.sort()
        for name in ans:
            print(name)
