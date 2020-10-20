def totalOverlaps(intervals):
    intervals.sort()
    n = len(intervals)
    count = 0
    for i in range(n):
        for y in range(i+1, n): 
            if intervals[i][0] == intervals[y][0] or intervals[i][1] > intervals[y][0]:
                count += 1
            else:
                pass
    return count


listIntervals = [[1,2],[1,2],[1,2]]
print(totalOverlaps(listIntervals))

