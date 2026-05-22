def is_isogram(string):
    #your code here
    if not string:
        return True
    string = string.lower()
    
    seen = []
    for char in string:
        if char in seen:
            return False
        seen.append(char)
    return True