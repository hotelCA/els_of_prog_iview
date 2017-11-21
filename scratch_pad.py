import collections

def print_permutation(A, chosen=[]):
    counter = 1
    def permutation(A, chosen):
        nonlocal counter
        if not A:
            print('{}: {}'.format(counter, chosen))
            counter += 1
            return
        for i in range(len(A)):
            permutation(A[:i] + A[i+1:], chosen + [A[i]])

    permutation(A, chosen)

def permutation_iteratively(A):
    q = collections.deque([A])
    current_permutation = []
    count = 1
    while q:
        X = q.pop()
        if X == []:
            print('{}: {}'.format(count, [i[1] for i in current_permutation]))
            count += 1
        elif len(A) - len(current_permutation) == len(X):
            Y = X[1:]
            current_permutation.append((0, X[0]))
            q.append(X)
            q.append(Y)
        elif current_permutation[-1][1] == X[-1]:
            del current_permutation[-1]
        else:
            i = current_permutation[-1][0]
            Y = X[:i+1] + X[i+2:]
            current_permutation[-1] = (i+1, X[i+1])
            q.append(X)
            q.append(Y)

permutation_iteratively(['a', 'b', 'c', 'd'])

