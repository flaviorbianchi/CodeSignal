def adjacentElementsProduct(inputArray):
    
    # initilize vars to measure array length, iterator initial position and largest product.
    length = len(inputArray)-1
    current = 0
    largest = -1000001 # smallest value-1 based on input

    # loop through array multiplying adjacent elements to find the largest product.
    while (current < length):
        product = inputArray[current] * inputArray[current + 1]
        if (product > largest):
            largest = product
        current += 1
    
    return largest

inputArray = [3, 6, -2, -5, 7, 3] # 21
# inputArray = [-1, -2] # 2

result = adjacentElementsProduct(inputArray)

print(result)