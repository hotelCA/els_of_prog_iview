import math

def find_sqrt(x):
    y = 1 / x if 0 < x < 1 else x
    dividend = current = y * 0.5
    
    while not math.isclose(current * current, y):
        dividend *= 0.5
        if current * current > y:
            current -= dividend
        else:
            current += dividend

    return 1/current if 0 < x < 1 else current
    
print(find_sqrt(15.0))