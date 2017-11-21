def test_well_formedness(S):
    opening, lookup = [], {'(' : ')', '[' : ']', '{' : '}'}
    for c in S:
        if c in lookup:
            opening.append(c)
        elif not opening or lookup[opening.pop()] != c:
            return False
    return not opening

S = '[][]([{}]))'
print(test_well_formedness(S))