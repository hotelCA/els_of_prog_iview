class ISBNTableEntry:
    def __init__(self, ISBN, price):
        self.price = price
        self.ISBN = ISBN
        self.newer = None
        self.older = None

class ISBNTable:
    TABLE_SIZE = 10
    def __init__(self):
        self.count = 0
        self.newest = None
        self.oldest = None
        self.table = {}
        
    def lookup(self, ISBN):
        if ISBN not in self.table:
            return None
        self.table[ISBN].older.newer = self.table[ISBN].newer
        self.table[ISBN].newer.older = self.table[ISBN].older
        self.table[ISBN].older = self.newest
        self.newest.newer = self.table[ISBN]
        self.newest = self.table[ISBN]
        self.newest.newer = None
        return self.table[ISBN]
        
    def insert(self, new_entry):
        if self.count == 0:
            self.oldest = new_entry
        else:
            if self.count == self.TABLE_SIZE:
                self.remove()
            new_entry.older = self.newest
            self.newest.newer = new_entry
        self.newest = new_entry
        self.table[new_entry.ISBN] = new_entry
        self.count += 1
        # print('[insert] newest {} oldest {}'.format(self.newest.price, self.oldest.price))
        # if self.count > 1:
            # print('[insert] newest.older {}'.format(self.newest.older.price))
        
    def remove(self):
        if self.count <= 0:
            raise IndexError('Table is empty.')
        self.count -= 1
        removed_entry = self.oldest
        self.oldest = self.oldest.newer
        if self.count > 0:
            self.oldest.older = None
        del self.table[removed_entry.ISBN]
        # print('[remove] newest {} oldest {}'.format(self.newest.price, self.oldest.price))
        # print('[remove] newest.older {}'.format(self.newest.older.price))

newTable = ISBNTable()
for i in range(1, 11):
    newTable.insert(ISBNTableEntry(i, 'price: {}'.format(i)))
print(newTable.lookup(15))
print(newTable.lookup(8))
current = newTable.newest
for i in range(0, newTable.count):
    print(current.price)
    current = current.older
# print(newTable.table)
