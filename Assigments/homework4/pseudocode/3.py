def findMaxArea(points):
    n = points.length
    max = 0
    current = 0

    start = 0
    
    for i in range(n):

        current += points[i].y
        
        if current > max:
            max = current
            optimal = (points[start].x, points[i].x)
        
        if current < 0:
            current = 0
            start = i + 1
    
    return optimal