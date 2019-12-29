def centuryFromYear(year):
    if (year <= 100):
        return 1
    
    century = int(year / 100)
    
    if (year % 100) > 0:
        century = century + 1

    return century

print(centuryFromYear(1900))