def findFlawedFuse(fuses):
    n = len(fuses)
    
    if n == 1:
        return fuses[0]
    
    step = determineStepSize(n)
    start = 0
    
    while start < n:
        end = min(start + step, n)
        
        if isCircuitOperational(fuses[start:end]):
            return findFlawedFuse(fuses[end:])
        
        start += step

    return fuses[n - 1]

def determineStepSize(n):
    #sPECIFFIC CONSTANT
    return 1

def isCircuitOperational(subset):
    #if electricity reaches end:
    #   return True
    #else:
    #   return False
    return False