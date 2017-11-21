def find_smallest_subset(A):
    A.sort()
    result = []
    cursor = A[0][0]
    end_time = A[-1][1]
    first_covered_task = 0
    last_covered_task = 0

    while cursor <= end_time and last_covered_task <= len(A) - 1:
        if last_covered_task == len(A) - 1:
            result.append(cursor)
            break
        while A[last_covered_task + 1][0] == cursor:
            last_covered_task += 1
            if last_covered_task == len(A) - 1:
                break
        for i in range(first_covered_task, last_covered_task+1):
            if A[i][1] == cursor:
                last_covered_task = last_covered_task + 1
                first_covered_task = last_covered_task
                result.append(cursor)
                break
        cursor += 1

    return result

A = [(1,2),(2,3),(2,3),(3,4),(3,4),(5,6)]
print(find_smallest_subset(A))