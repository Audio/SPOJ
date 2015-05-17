# http://aditya.vaidya.info/blog/2014/06/27/modular-exponentiation-python/

lines = int(input())
for i in range(lines):
    ab = input().split(' ')
    a = int(ab[0])
    b = int(ab[1])
    print( pow(a, b, 10) )

