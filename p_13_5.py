import collections

Interval = collections.namedtuple('Interval', ('start', 'end'))


def find_largest_overlap(A):
    largest = 0
        
    for i in range(0,24):
        current_hour_overlap = 0
        for interval in A:
            if interval.start <= i and interval.end >= i:
                current_hour_overlap += 1
        if current_hour_overlap > largest:
            largest = current_hour_overlap
    return largest
    
A = [Interval(1,2),
    Interval(2,4),
    Interval(3,6),
    Interval(4,8),
    Interval(7,8),
    Interval(10,21)]
print(find_largest_overlap(A))