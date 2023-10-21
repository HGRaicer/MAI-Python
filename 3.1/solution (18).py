import math

stack = []

strr = list(input().split(" "))

for elem in strr:
    if not (elem in ["+", "-", "*", "/", "!", "#", "@", "~"]):
        stack.append(elem)
    else:
        if elem == "+":
            numb1 = int(stack[-2])
            stack.pop(-2)
            numb2 = int(stack[-1])
            stack.pop(-1)
            stack.append(numb1 + numb2)
        if elem == "-":
            numb1 = int(stack[-2])
            stack.pop(-2)
            numb2 = int(stack[-1])
            stack.pop(-1)
            stack.append(numb1 - numb2)
        if elem == "*":
            numb1 = int(stack[-2])
            stack.pop(-2)
            numb2 = int(stack[-1])
            stack.pop(-1)
            stack.append(numb1 * numb2)
        if elem == "/":
            numb1 = int(stack[-2])
            stack.pop(-2)
            numb2 = int(stack[-1])
            stack.pop(-1)
            stack.append(numb1 / numb2)
        if elem == "!":
            numb2 = int(stack[-1])
            stack.pop(-1)
            stack.append(math.factorial(numb2))
        if elem == "#":
            numb2 = int(stack[-1])
            stack.append(numb2)
        if elem == "@":
            numb1 = int(stack[-2])
            stack.pop(-2)
            numb2 = int(stack[-1])
            stack.pop(-1)
            stack.append(numb1 * numb2)

print(stack[0])
