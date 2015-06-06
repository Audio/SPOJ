while True:
    line = input()
    if line == '0 0': break

    attacking = [ int(n) for n in input().split(' ') ]
    defending = [ int(n) for n in input().split(' ') ]

    attacking.sort()
    defending.sort()

    if attacking[0] < defending[0] or attacking[0] < defending[1]:
        print('Y')
    else:
        print('N')
