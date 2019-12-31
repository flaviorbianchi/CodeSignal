def makeArrayConsecutive2(statues):
    statues.sort()

    # create another list with all the values from 1st to last numbers in statues
    current = statues[0]
    last = statues[-1]

    full = []
    while current < last:
        full.append(current)
        current += 1

    return len([x for x in full if x not in statues])

statues = [6, 2, 3, 8]
result = makeArrayConsecutive2(statues)
print(result)
