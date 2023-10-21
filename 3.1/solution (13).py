all_numbs = list(map(int, input().split()))

poww = int(input())

for numb in all_numbs:
    print(pow(numb, poww), end=" ")
