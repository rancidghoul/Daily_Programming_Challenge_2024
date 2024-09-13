def Leaders(arr):
    n = len(arr)
    if n == 0:
        return []
    
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)

    for i in range(n-2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            leaders.append(max_right)

    leaders.reverse()
    return leaders

