def makeArrayConsecutive(sequence):
    sequence.sort()

    # create another list with all the values from 1st to last numbers in sequence
    current = sequence[0]
    last = sequence[-1]

    full = []
    while current < last:
        full.append(current)
        current += 1

    return [x for x in full if x not in sequence]


sequence = [6, 2, 3, 8]
result = makeArrayConsecutive(sequence)
print(result)