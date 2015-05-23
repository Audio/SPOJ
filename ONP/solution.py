def solve(expr):
    global i
    arg1 = arg2 = op = None
    while i < len(expr):
        c = expr[i]
        i += 1

        if c == '(':
            subexpr = solve(expr)
            if i >= len(expr):
                return subexpr
            elif arg1 == None:
                arg1 = subexpr
            else:
                arg2 = subexpr

        elif c == ')':
            return arg1 + arg2 + op

        elif arg1 == None:  arg1 = c
        elif  op  == None:   op  = c
        elif arg2 == None:  arg2 = c

    return expr

lines = int(input())
for l in range(lines):
    i = 0
    print(solve(input()))

