def two_sum(numbers, target):
    hash_map = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        if complement in hash_map:
            return (hash_map[complement], i)
        
        hash_map[num] = i