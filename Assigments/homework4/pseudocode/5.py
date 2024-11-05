def resourceAllocation(tasks):
    if len(tasks) == 1:
        return tasks[0], tasks[0]

    mid = len(tasks) // 2

    leftHalf = tasks[:mid]
    rightHalf = tasks[mid:]

    leftMax, leftMin = resourceAllocation(leftHalf)
    rightMax, rightMin = resourceAllocation(rightHalf)
    
    maxx = max(leftMax, rightMax)
    minn = min(leftMin, rightMin)

    return maxx, minn