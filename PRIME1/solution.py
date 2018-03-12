from math import ceil, sqrt

def sieve(to_num):
    is_prime = [True] * (to_num + 1)
    primes = []
    for num in range(to_num + 1):
        if not is_prime[num]:
            continue

        if num < 2:
            is_prime[num] = False
            continue

        for multi in range(num * 2, to_num + 1, num):
            is_prime[multi] = False

        primes.append(num)

    return primes

def get_interested_intervals(min_segment_value, max_segment_value):
    interested = []
    for interval in intervals:
        if interval['from_num'] <= max_segment_value and interval['to_num'] >= min_segment_value:
            interested.append(interval)

    return interested

def segmented_sieve(to_num):
    max_segment_size = ceil(sqrt(to_num))
    primes = sieve(max_segment_size)

    for prime in primes:
        for interval in intervals:
            if prime >= interval['from_num'] and prime <= interval['to_num']:
                interval['primes'].append(prime)

    for segment in range(1, ceil(to_num / max_segment_size)):
        min_segment_value = segment * max_segment_size
        max_segment_value = min(min_segment_value + max_segment_size, to_num + 1) - 1

        interested_intervals = get_interested_intervals(min_segment_value, max_segment_value)
        # print(min_segment_value, max_segment_value, interested_intervals)
        if len(interested_intervals) == 0: continue

        segment_size = max_segment_value - min_segment_value + 1
        is_prime = [True] * segment_size

        max_segment_value_sqrt = ceil(sqrt(max_segment_value))
        for prime in primes:
            if prime > max_segment_value:
                break

            multi = min_segment_value - (min_segment_value % prime)
            if multi < min_segment_value: multi += prime
            while multi <= max_segment_value:
                is_prime[multi - min_segment_value] = False
                multi += prime

        for index, value in enumerate(is_prime):
            if value is True:
                prime = min_segment_value + index
                for interval in interested_intervals:
                    if prime >= interval['from_num'] and prime <= interval['to_num']:
                        interval['primes'].append(prime)

intervals = []
to_nums = []

tests_count = int(input())
for t in range(tests_count):
    raw = input().split()

    interval = {}
    interval['from_num'] = int(raw[0])
    interval['to_num'] = int(raw[1])
    interval['primes'] = []
    intervals.append(interval)

    to_nums.append(interval['to_num'])

segmented_sieve(max(to_nums))

for interval in intervals:
    print('\n'.join(map(str, interval['primes'])))
    print()
