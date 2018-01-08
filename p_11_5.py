import math

def find_sqrt(x):
    x = 1 / x if 0 < x < 1 else x
    dividend = current = x / 2
    
    while not math.isclose(current * current, x):
        dividend /= 2
        if current * current > x:
            current = current + dividend
        else:
            current = current - divident

    return 1/current if 0 < x < 1 else current 
    
print(find_sqrt(16))