def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    str=0
    while i<len(s):
        if s[i].isupper():
            str+=1
        i+=1
    return str
print(main("Hello World 2023"))