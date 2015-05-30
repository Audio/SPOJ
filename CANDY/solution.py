while True:
    packets_count = int(input())
    if packets_count == -1: break

    packets = []
    sum = 0
    for p in range(packets_count):
        candies = int(input())
        packets.append(candies)
        sum += candies

    per_packet = sum / len(packets)
    if per_packet % 1 != 0:
        print('-1')
    else:
        moves = 0
        per_packet = int(per_packet)
        for p in packets:
            if p > per_packet:
                moves += p - per_packet
        print(moves)
