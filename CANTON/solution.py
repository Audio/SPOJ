import math

lines = int(input())
for l in range(lines):
    n = int(input())

    # get diagonal number (e.g. on what diagonal the "n" lies)
    # expressed from arithmetic progression sum equation
    diag = math.ceil((math.sqrt((n * 2 * 4 + 1)) - 1) / 2)

    # get sum of numbers on all previous diagonals
    diag_sum = diag * (diag - 1) // 2

    # get the top-right number (visually) that lies on diag
    # diagonal direction is important
    incr = 1 if (diag % 2 == 0) else diag
    top_right_n = diag_sum + incr

    # count diff from top-right number to n
    diff = abs(n - top_right_n)

    # print result
    row = 1 + diff
    column = diag - diff
    print('TERM %d IS %d/%d' % (n, row, column))

