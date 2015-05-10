"""
V = a**2 * SIN_60 * h/2
implies that
 h = 2*V / (a**2 * SIN_60)
which can be used in
 S = a**2 * SIN_60 + 3*a*h
like
 S = a**2 * SIN_60 + 6*V/(a*SIN_60)
which can be simplified as
 S = math.sqrt(3) * (a**3 + 8V) / 2*a
and wolfram alpha says it's derivative is
 da = math.sqrt(3) * (a**3 - 4*V) / a**2
so locale extrema are for
 (1) a = 0
 (2) a = cube root of 4*V
in case (1) V is always 0, so (2) is the winner
and therefore optimal "a" can be calculated as (2)
"""

import math

SIN_60 = math.sin(math.radians(60))

def S(V):
    a = math.pow(4*V, 1 / 3.0)
    return a**2 * SIN_60 + 6*V/(a*SIN_60)

lines = int(input())
for i in range(lines):
    V = int(input())
    print("%.10f" % S(V))


