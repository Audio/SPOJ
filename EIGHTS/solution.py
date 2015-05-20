# observed while slowly generating ultra big cache:
#  192+n*250 always ends with "888"

lines = int(input())
for l in range(lines):
    k = int(input())
    print(192 + (k-1) * 250)

