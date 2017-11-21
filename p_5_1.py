def dutch_flag(sub_array, index):
    smallest = walker = middle = 0
    largest = len(sub_array) - 1
    pivot = sub_array[index]

    while walker <= largest:
        if sub_array[walker] < pivot:
            sub_array[walker], sub_array[smallest] = sub_array[smallest], sub_array[walker]
            smallest, walker = smallest + 1, walker + 1
        elif sub_array[walker] > pivot:
            sub_array[walker], sub_array[largest] = sub_array[largest], sub_array[walker]
            largest -= 1
        else:
            walker += 1
    return sub_array

def dutch_flag_4(sub_array):
    smallest = smaller = walker = 0
    largest = len(sub_array) - 1

    while walker <= largest:
        if sub_array[walker] == 1:
            sub_array[walker], sub_array[smallest] = sub_array[smallest], sub_array[walker]
            smallest += 1
            if smallest > walker:
                walker += 1
            if smallest > smaller:
                smaller += 1
        elif sub_array[walker] == 2:
            sub_array[walker], sub_array[smaller] = sub_array[smaller], sub_array[walker]
            smaller, walker = smaller + 1, walker + 1
        elif sub_array[walker] == 4:
            sub_array[walker], sub_array[largest] = sub_array[largest], sub_array[walker]
            largest -= 1
        else:
            walker += 1
    return sub_array

print(dutch_flag([3,2,3,2,2,3,1,2,1,7,1,2,3,5,2,3], 3))
print(dutch_flag_4([3,2,3,2,2,3,1,2,1,4,1,2,3,4,2,3]))
print('Name {name}, rank {rank}'.format(name='Jon', rank=6))
print(5 // 2)