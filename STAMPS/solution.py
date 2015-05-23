scenarios = int(input())
for s in range(scenarios):
    line = input().split(' ')
    need = int(line[0])
    friends = int(line[1])
    offers = [ int(o) for o in input().split(' ') ]
    offers.sort(reverse=True)

    borrows = 0
    o = 0
    while need > 0:
        need -= offers[o]
        borrows += 1
        o += 1
        if o >= len(offers):
            break

    if need > 0:
        borrows = 'impossible'

    print("Scenario #%d:\n%s\n" % (s+1, borrows))

