from string import ascii_lowercase

# http://stackoverflow.com/q/1336791/557223
class Word(object):
    __slots__ = ('l')
    def __init__(self, l):
        self.l = l
    def __repr__(self):
        return self.l

# DFS
def visit(words, visited):
    for w in words:
        visited.add(w)
        if len(visited) == words_count:
            raise ValueError('Solution found')

        succs = [s for s in by_f[w.l] if s not in visited]
        if len(succs):
            visit(succs, visited)

        visited.remove(w)

tests_count = int(input())
for t in range(tests_count):

    by_f = {}
    for c in ascii_lowercase:
        by_f[c] = []

    words_count = int(input())
    words = [None] * words_count
    for id in range(words_count):
        word = input()
        f = word[0]
        l = word[-1:]
        word = Word(l)
        words[id] = word
        by_f[f].append(word)

    try:
        visited = set()
        visit(words, visited)
        print('The door cannot be opened.')
    except ValueError as found:
        print('Ordering is possible.')

