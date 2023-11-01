import itertools

line = input()
l1_line = line.split()
variables = set()
operations = ['and', 'or', 'not']
for symb in l1_line:
    if symb not in operations:
        variables.add(symb)
variables = sorted(list(variables))
gl_dict = {}
for symb in variables:
    gl_dict[symb] = None
    print(symb, end=" ")
print("F")
bin_list = itertools.product([0, 1], repeat=len(variables))
for ans in bin_list:
    for idx in range(len(ans)):
        gl_dict[variables[idx]] = ans[idx]
        print(ans[idx], end=" ")
    if eval(line, gl_dict) == 1:
        print(1)
    else:
        print(0)
