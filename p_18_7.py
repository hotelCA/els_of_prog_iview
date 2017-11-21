import collections
# Better approach is to find all the combinations of letters that differ from the target by one character
# and see if it's in the dictionary
def find_production_seq(D, s, t):
    if s not in D or t not in D:
        return -1

    examined = set()
    Q = collections.deque([(s, 0)])

    while Q:
        target, time = Q.popleft()
        if target == t:
            return time

        examined.add(target)

        for w in filter(lambda x: x not in examined, D):
            for i in range(len(target)):
                if (w[:i] + w[i+1:]) == (target[:i] + target[i+1:]):
                    Q.append((w, time + 1))
                    break

    return -1

D = ['cat', 'cot', 'eat', 'dot', 'cog', 'dog', 'chair', 'cheat', 'dim', 'cip']
print(find_production_seq(D, 'dog', 'eat'))

