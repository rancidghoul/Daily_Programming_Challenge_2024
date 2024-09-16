def reversestring(s:str) -> str:
    words = s.split()
    reversed_string = words[::-1]
    return ' '.join(reversed_string)

