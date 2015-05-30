def solve(needle, haystack):
    start = 0
    out = ''
    while True:
        start = haystack.find(needle, start)
        if start == -1: break
        out += str(start) + "\n"
        start += 1
    print(out)

while True:
    try:
        input()
        solve(input(), input())
    except EOFError:
        break
