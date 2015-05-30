cache = {}
def longest(from_index):
    if cache.get(from_index) != None: return cache[from_index]

    next_paths = []
    for next_index in range(from_index+1, len(nums)):
        if nums[from_index] < nums[next_index]:
            next_paths.append(longest(next_index))

    cache[from_index] = 1 + max(next_paths) if len(next_paths) else 1

    return cache[from_index]


input() # skip the first line

nums = [ int(n) for n in input().split(' ') ]
results = [ longest(i) for i in range(len(nums)) ]
print(max(results))
