def almostIncreasingSequence(sequence):
    for value in sequence:
        #create copy of sequence and remove current value
        sequenceCopy = sequence.copy()
        sequenceCopy.remove(value)
        
        counter = 0
        while (counter < len(sequence)-1):
            if (sequenceCopy[counter] <= sequenceCopy[counter+1]):
                return False
            counter += 1
    
    return True