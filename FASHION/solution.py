tests = int(input())
for t in range(tests):
    count = int(input())

    men = [ int(m) for m in input().split(' ') ]
    women = [ int(w) for w in input().split(' ') ]
    men.sort()
    women.sort()

    sum = 0
    for c in range(count):
        sum += men[c] * women[c]

    print(sum)

