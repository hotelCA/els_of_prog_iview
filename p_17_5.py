# This function assumes there IS a majority elecment.
def find_majority_element(A):
    majority_el = None
    count = 1
    for a in A:
        if a != majority_el:
            if count == 1:
                majority_el = a
            else:
                count -= 1
        else:
            count += 1
            
    return majority_el
    
A = [1,2,3,2,3,2,2,1,2]
print(find_majority_element(A))
        