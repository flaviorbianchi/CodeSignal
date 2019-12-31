def fractionComparison(a, b):
    fractA = a[0]/a[1]
    fractB = b[0]/b[1]
    if (fractA > fractB):
        return '>'
    elif (fractA == fractB):
        return '='
    else:
        return '<'
