strr = input().lower()

arr_str = list(strr.split(" "))
new_str = "".join(arr_str)

if new_str == new_str[::-1]:
    print("YES")
else:
    print("NO")
