def mult_3_or_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False
     
def solution(number):
    result = []
    if number < 0:
        return 0
    
    for i in range(0,number):
        if mult_3_or_5(i):
            result.append(i)
    return sum(result)