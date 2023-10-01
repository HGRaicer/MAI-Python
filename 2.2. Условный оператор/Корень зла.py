a = float(input())
b = float(input())
c = float(input())
if abs(a - b) <= 0.00001 and abs(a - c) <= 0.00001 and abs(a - 0) <= 0.00001:
    print("Infinite solutions")

else:
    if abs(a - 0) <= 0.00000001:
        if abs(b - 0) <= 0.00000001:
            print("No solution")
        else:
            print(-c / b)

    else:
        d = b * b - 4 * a * c
        if d < 0:
            print("No solution")
        else:
            x1 = (-b + d**0.5) / (2 * a)
            x2 = (-b - d**0.5) / (2 * a)
            if abs(x1 - x2) <= 0.0000001:
                print(x1)
            else:
                k = [x1, x2]
                k.sort()
                print(f"{k[0]:.2f} {k[1]:.2f}")

