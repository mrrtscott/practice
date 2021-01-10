cache = {}

def gridTrav(m, n):
    key = (str(m) + "," + str(n))
    if key in cache:
        return cache[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    cache[key] =  gridTrav(m -1, n) + gridTrav(m, n-1)
    return cache[key]
    


print (gridTrav(18,18))  