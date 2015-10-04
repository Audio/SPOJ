from string import ascii_lowercase

'''
A directed graph has an Eulerian trail if and only if
at most one vertex has (out-degree) − (in-degree) = 1,
at most one vertex has (in-degree) − (out-degree) = 1,
every other vertex has equal in-degree and out-degree,
and all of its vertices with nonzero degree belong to
a single connected component of the underlying undirected graph.
'''

class Char(object):
    def __init__(self, char):
        self.char = char
        self.links = set()
        self.links_in = 0
        self.links_out = 0

    def __repr__(self):
        link_chars = []
        for l in self.links:
            link_chars.append(l.char)
        link_chars = ",".join(sorted(link_chars))
        return "%s(links:%s,in:%i,out:%i)" % (self.char, link_chars, self.links_in, self.links_out)

def is_connected(chars):
    visited = set()
    queue = [chars[0]]
    while len(queue):
        char = queue.pop()
        visited.add(char)
        for linked_char in char.links:
            if linked_char not in visited:
                queue.append(linked_char)

    return len(visited) == len(chars)

def has_eulerian_path(chars):
    starts = 0
    ends = 0
    for char in chars:
        diff = char.links_in - char.links_out
        if abs(diff) > 1:
            return False
        elif diff == -1:
            starts += 1
        elif diff == 1:
            ends += 1

    return starts == ends and starts <= 1

tests_count = int(input())
for t in range(tests_count):
    chars = {}
    for c in ascii_lowercase:
        chars[c] = Char(c)

    words_count = int(input())
    for id in range(words_count):
        word = input()
        f = word[0]
        l = word[-1]
        chars[f].links_out += 1
        chars[l].links_in += 1
        chars[f].links.add(chars[l])
        chars[l].links.add(chars[f])

    used_chars = []
    for c, char in chars.items():
        if len(char.links) > 0:
            used_chars.append(char)
    # print('used chars', used_chars)

    if is_connected(used_chars) and has_eulerian_path(used_chars):
        print('Ordering is possible.')
    else:
        print('The door cannot be opened.')

