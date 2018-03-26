import collections

Interval = collections.namedtuple('Interval', ('start', 'end'))


class Endpoint:
    def __init__(self, value, closed):
        self.value = value
        self.closed = closed
        
    def __eq__(self, other):
        if isinstance(other, Endpoint):
            return self.value == other.value and self.closed == other.closed
        return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, Endpoint):
            if self.value < other.value:
                return True
            elif self.value == other.value:
                if not self.closed and other.closed:
                    return True
            return False
        return NotImplemented
    
        
def overlaps(end, x):
    if x.value < end.value:
        return True
    elif x.value == end.value:
        if x.closed or end.closed:
            return True
    return False

def create_disjoint_set(A):
    if len(A) < 2:
        return A
        
    start = A[0].start
    end = A[0].end
    result = []
    for x in A[:-1]:
        if overlaps(end, x.start):
            end = max(end, x.end)
        else:
            result.append(Interval(start, end))
            start = x.start
            end = x.end
    
    result.append(Interval(start, end))
    return result
    
A = [Interval(Endpoint(1, True), Endpoint(4, True)),
    Interval(Endpoint(3, True), Endpoint(6, True)),
    Interval(Endpoint(7, True), Endpoint(7, True)),
    Interval(Endpoint(8, True), Endpoint(10, False)),
    Interval(Endpoint(10, False), Endpoint(12, True)),
    Interval(Endpoint(12, False), Endpoint(14, True))]
    
R = create_disjoint_set(A)

for x in R:
    print('{}: {}, {}: {}'.format(x.start.closed, x.start.value, x.end.closed, x.end.value))
    