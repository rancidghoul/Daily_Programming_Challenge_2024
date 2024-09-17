def longestcommonprefix(strs):
    if not strs:
        return ""
    min_len = min([len(s) for s in strs])
    prefix = ""

    for i in range(min_len):
        char = strs[0][i]

        for string in strs:
            if string[i] != char:
                return prefix
            
        prefix += char

    return prefix
