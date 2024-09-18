def groupanagrams(strs):
    anagrams_map ={}

    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams_map:
            anagrams_map[sorted_str].append(s)
        else:
            anagrams_map[sorted_str] = [s]

    return list(anagrams_map.values())
            