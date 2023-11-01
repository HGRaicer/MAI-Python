import itertools

expression = f'({input()})'.replace("->", "<=").replace("~", "==").replace("^", "!=")
expression = expression.replace("(", "((").replace(")", "))").replace("==", ") == (")
expression = expression.replace("(", "((").replace(")", "))").replace("<=", ") <= (")
expression = expression.replace("(", "((").replace(")", "))").replace("!=", ") != (")
variables = sorted(list(set(i for i in expression if i.isupper())))
print(*variables, "F")
for combination in itertools.product([0, 1], repeat=len(variables)):
    gl_dict = {variable: value for variable, value in zip(variables, combination)}
    print(*combination, int(eval(expression, gl_dict)))