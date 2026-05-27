def solve(st):
    if len(st) % 2 != 0:
        return -1
    open_cnt = 0
    close_cnt = 0
    
    for char in st:
        if char == '(':
            open_cnt += 1
        else:
            if open_cnt > 0:
                open_cnt -= 1
            else:
                close_cnt += 1
                
    return (open_cnt +1) // 2 + (close_cnt +1) // 2
                