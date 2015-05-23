lines = int(input())
for l in range(lines):
    line = input().split(' ')
    health = int(line[0])
    armor = int(line[1])

    if health < 1 or armor < 1:
        print(0)
        continue

    steps = 0
    while True:
        if steps % 2 == 0:
            # air
            health += 3
            armor  += 2
        elif health > 5 and armor > 10:
            # water
            health -= 5
            armor  -= 10
        else:
            # fire
            health -= 20
            armor  += 5

        if health > 0 and armor > 0:
            steps += 1
        else:
            print(steps)
            break

