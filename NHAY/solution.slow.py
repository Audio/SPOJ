# explanation: https://www.youtube.com/watch?v=5i7oKodCRJo

def kmp_table(pattern):
    i = 0
    table = [0]
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i]
        if pattern[i] == pattern[j]:
            i += 1
        table.append(i)
    return table

def kmp(text, pattern):
    m = len(pattern)
    i = 0
    table = kmp_table(pattern)
    out = ''
    for j in range(0, len(text)):
        while i > 0 and pattern[i] != text[j]:
            i = table[i]
        if pattern[i] == text[j]:
            i += 1
        if i == m:
            out += str(j+1-m) + "\n"
            i = table[i-1]
    print(out)

while True:
    try:
        input()
        needle = input()
        haystack = input()
        kmp(haystack, needle)
    except EOFError:
        break
