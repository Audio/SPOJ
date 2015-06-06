while True:
    if input() == '-1': break

    peaks = [ int(n) for n in input().split(' ') ]
    heights = max(peaks) + 1 # including zero level
    widths  = len(peaks) - 1 # number of diffs

    picture = [[' ' for w in range(widths)] for h in range(heights)]

    for w in range(widths):
        prev_h = peaks[w]
        next_h = peaks[w+1]
        if next_h == prev_h:
            picture[heights - prev_h - 1][w] = '_'
        elif next_h > prev_h:
            picture[heights - prev_h - 1][w] = '/'
        else:
            picture[heights - prev_h][w] = '\\'

    for row in picture:
        line = ''.join(row).rstrip()
        if len(line): print(line)

    print('***')
