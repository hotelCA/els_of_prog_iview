from functools import reduce

def decode_spreadsheet_columns(s):
    
    return reduce((lambda sum, c: 26 * sum + (ord(c) - ord('A') + 1)), s, 0)

print(decode_spreadsheet_columns('AA'))