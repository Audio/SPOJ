def hash(key):
    sum = 0
    for index, char in enumerate(key):
        sum += ord(char) * (index + 1)
    return (19 * sum) % 101

def insert(key, value):
    for j in range(20):
        final_key = (key + j * j + 23 * j) % 101
        if table.get(final_key, value) == value:
            table[final_key] = value
            return final_key
    return None
 
table = None
used_values = None
tests_count = int(input())
for t in range(tests_count):

    table = {}
    used_values = {}
    op_count = int(input())
    for o in range(op_count):

        line = input().split(':')
        cmd = line[0]
        value = line[1]

        if cmd == 'ADD':
            if value not in used_values:
                key = insert(hash(value), value)
                if key != None:
                    used_values[value] = key

        elif cmd == 'DEL':
            key = used_values.get(value, None)
            if key != None:
                del table[key]
                del used_values[value]

    print(len(table))
    for key in sorted(table.keys()):
        print(str(key) + ':' + table[key])
