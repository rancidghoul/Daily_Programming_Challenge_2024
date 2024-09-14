def zerosubarrays(arr):
    prefix_sum_map = {}
    result = []
    prefix_sum = 0
    prefix_sum_map[0] = [-1]

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum in prefix_sum_map:
            for start_idx in prefix_sum_map[prefix_sum]:
                result.append((start_idx+1, i))

        if prefix_sum in prefix_sum_map:
            prefix_sum_map[prefix_sum].append(i)
        else:
            prefix_sum_map[prefix_sum] = [i]

    return result

