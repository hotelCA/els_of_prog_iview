import collections

Interval = collections.namedtuple('Interval', ('start', 'end'))
EndpointAndTime = collections.namedtuple('EndpointAndTime', ('value', 'type'))

def find_largest_overlap(A):
    endpoints = []

    # prepare endpoints
    for interval in A:
        endpoints.append(EndpointAndTime(value=interval.start, type='start'))
        endpoints.append(EndpointAndTime(value=interval.end, type='end'))

    running_sum = 0
    max_overlap = 0

    # enumerate through the sorted endpoints
    for endpoint in sorted(endpoints):
        print(endpoint.type)
        if endpoint.type == 'start':
            running_sum += 1
        else:
            running_sum -= 1

        max_overlap = max(running_sum, max_overlap)

    print(max_overlap)


A = [Interval(1,2),
    Interval(2,4),
    Interval(3,6),
    Interval(4,8),
    Interval(7,8),
    Interval(10,21)]

print(find_largest_overlap(A))
