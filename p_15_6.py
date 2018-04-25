def match_parens(n):
    def _match_parens(prefix, num_open, num_close):
        nonlocal n
        if num_close == n:
            print(prefix)
        else:
            if num_open < n:
                _match_parens(prefix + '(', num_open + 1, num_close)
            if num_open > num_close:
                _match_parens(prefix + ')', num_open, num_close + 1)
                
    if n == 0:
        return ''
    else:
        _match_parens('', 0, 0)
        
match_parens(4)
    
    