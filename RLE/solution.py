import sys

def encode(string):
    prev_char = None
    count = 0
    output = ''
    for char in string:
        if prev_char == None:
            prev_char = char

        if char != prev_char:
            if count > 3:
                output += str(count) + '!' + prev_char
            else:
                for i in range(count):
                    output += prev_char

            prev_char = char
            count = 0

        count += 1

    if count > 3:
        output += str(count) + '!' + prev_char
    else:
        for i in range(count):
            output += prev_char

    return output

for line in sys.stdin:
    print(encode(line.rstrip()))
