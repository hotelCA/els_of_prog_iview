def find_sqrt(x):
    lower, upper = 0, x
    while upper >= lower:
        current = (upper + lower) // 2
        if current * current > x:
            upper = current - 1
        else:
            lower = current + 1

    return upper
    
print(find_sqrt(16))