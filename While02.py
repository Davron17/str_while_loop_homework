def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    str=0
    while i<len(s):
        if s[i].isalpha():
            str+=1
        i+=1
    return str
print(main("hello world 2023"))




    