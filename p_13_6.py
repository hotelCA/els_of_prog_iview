import collections

Interval = collections.namedtuple('Interval', ('start', 'end'))


def union(A, x):
    start_index = 0

    while start_index < len(A) and A[start_index].end < x.start:
        start_index += 1

    end_index = start_index

    while end_index < len(A) and A[end_index].start <= x.end:
        end_index += 1

    if start_index != end_index:
        x = Interval(min(A[start_index].start, x.start), max(A[end_index-1].end, x.end))

    return A[:start_index] + [x] + A[end_index:]


A = [Interval(7, 10),
     Interval(12, 18),
     Interval(22, 26),
     Interval(30, 38)]

x = Interval(8, 22)

print(union(A, x))