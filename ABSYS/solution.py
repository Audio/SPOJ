word = 'machula'

def fix(eq):
    parts = eq.split(' ')
    if parts[0].find(word) > -1:
        parts[0] = str(int(parts[4]) - int(parts[2]))
    elif parts[2].find(word) > -1:
        parts[2] = str(int(parts[4]) - int(parts[0]))
    else:
        parts[4] = str(int(parts[0]) + int(parts[2]))

    return ' '.join(parts)

lines = int(input())
for i in range(lines):
    input() # skip blank line
    equation = input()
    print(fix(equation))

