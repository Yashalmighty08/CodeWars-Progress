def solution(s):
    result = []
    for i in range(0, len(s),2):
        if i +1 < len(s):
            result.append(s[i] +s[i+1])
        else:
            result.append(s[i] + '_')
    return result