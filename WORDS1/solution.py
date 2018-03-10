from array import array

'''
A directed graph has an Eulerian trail if and only if
at most one vertex has (out-degree) − (in-degree) = 1,
at most one vertex has (in-degree) − (out-degree) = 1,
every other vertex has equal in-degree and out-degree,
and all of its vertices with nonzero degree belong to
a single connected component of the underlying undirected graph.
'''

UNSIGNED_BYTE = 'L'
ALPHABET_LENGHT = 26

def debug(connections, in_degrees, out_degrees):
    charConnections = {}
    for i in connections:
        char = num_to_char(i)
        connected = set()
        for j in connections[i]:
            connected.add(num_to_char(j))
        charConnections[char] = connected
    print('connections:', charConnections)

def empty_array():
    return array(UNSIGNED_BYTE, [0] * ALPHABET_LENGHT)

def char_to_num(char):
    return ord(char) - ord('a')

def num_to_char(num):
    return chr(num + ord('a'))

def is_connected(connections):
    visited = set()
    used_char = next(iter(connections))
    queue = [used_char]
    while len(queue):
        char = queue.pop()
        visited.add(char)
        for linked_char in connections[char]:
            if linked_char not in visited:
                queue.append(linked_char)

    return len(visited) == len(connections)

def has_eulerian_path(in_degrees, out_degrees):
    ends = 0
    for char in range(ALPHABET_LENGHT):
        diff = abs(in_degrees[char] - out_degrees[char])
        if abs(diff) > 1: return False
        if diff == 1: ends += 1

    return ends == 0 or ends == 2

tests_count = int(input())
for t in range(tests_count):
    connections = {}
    out_degrees = empty_array()
    in_degrees = empty_array()

    words_count = int(input())
    for id in range(words_count):
        word = input()
        f = char_to_num(word[0])
        l = char_to_num(word[-1])
        out_degrees[f] += 1
        in_degrees[l] += 1
        if f not in connections: connections[f] = set()
        connections[f].add(l)
        if l not in connections: connections[l] = set()
        connections[l].add(f)

    # debug(connections, in_degrees, out_degrees)

    if is_connected(connections) and has_eulerian_path(in_degrees, out_degrees):
        print('Ordering is possible.')
    else:
        print('The door cannot be opened.')
