from math import ceil, floor

def get_max_distance(positions, block_count):
    distances = get_distances(positions)
    max_possible_distance = get_max_possible_distance(positions, block_count)
    tip = max_possible_distance
    last_successful_tip = 1
    while True:
        if fact_or_fiction(distances, block_count, tip):
            if tip == max_possible_distance:
                return tip

            last_successful_tip = tip
            tip += ceil((max_possible_distance - tip) / 2)
        else:
            if tip == last_successful_tip + 1:
                return last_successful_tip

            max_possible_distance = tip - 1
            tip = floor((tip - last_successful_tip) / 2)

def get_distances(positions):
    distances = []
    for index in range(1, len(positions)):
        distances.append(positions[index] - positions[index - 1])
    return distances

def get_max_possible_distance(positions, block_count):
    first_position = positions[0]
    last_position = positions[len(positions) - 1]
    return floor((last_position - first_position) / block_count)

def fact_or_fiction(distances, required_block_count, required_block_size):
    block_count = 0
    block_size = 0
    for distance in distances:
        block_size += distance

        if block_size >= required_block_size:
            block_count += 1
            block_size = 0

            if block_count >= required_block_count:
                return True

    return False

tests_count = int(input())
for t in range(tests_count):
    raw = input().split()

    stalls = int(raw[0])
    cows = int(raw[1])
    block_count = cows - 1

    positions = []
    for s in range(stalls):
        positions.append(int(input()))

    result = get_max_distance(sorted(positions), block_count)
    print(result)
