"""
Create a hash table that allows getting and setting key-value pairs

Comparison to arrays:
Faster search, insertion and deletion (O(1) vs O(n))
(Same lookup (O(1)), no push (?))
But unordered
"""

class HashTable():
    def __init__(self, size):
        # self.values = []
        self.size = size
        self.values = [None] * size

    '''
    def hash(self, key):         # TODO (maggie.liuzzi): implement custom hash function in Python
        hashed_key = 0
        for i in range(len(key)):
            hashed_key = (hashed_key + unicode(key[i]) * i) % len(self.values)
        print(hashed_key)
        return hashed_key
        # return unicode(key) % len(self.values)

    def __private_method(self):  # print(hash_table.__private_method()) - AttributeError: 'HashTable' object has no attribute '__private_method'
        return 0
    def private_method(self):
        return 1
    def testing_private_method(self):
        return self.__private_method()
    '''

    def get_hash_key(self, key):  # Time: O(1)
        return hash(key) % self.size  # hashed_key could be the address in memory  # TODO: compare with built-in hash()

    def set_value(self, key, value):  # Time: O(1)
        hash_key = self.get_hash_key(key)
        print("key: {}, value: {}, hashed_key: {}".format(key, value, hash_key))
        # self.values.insert(hash_key, value)
        # self.values[hash_key] = value  # not dealing with collisions, just overriding entry
        if not self.values[hash_key]:
            self.values[hash_key] = [[key, value]] # not dealing with collisions - TODO (maggie.liuzzi): 
        else:
            self.values[hash_key].extend([[key, value]])

    def get_value(self, key):  # O(1) if no collisions - could be O(n) in our case
        hash_key = self.get_hash_key(key)  # address
        if not self.values[hash_key]:
            # print("Key not in hash table")
            return None
        # value = self.values[hash_key]  # not dealing with collisions
        for pair in self.values[hash_key]:  # will get the first occurrence - if last is preferred, loop in reverse  # Why not just a list of values in a sort of dictionary?
            if pair[0] == key:
                return pair[1]

    def get_values(self):
        return self.values

    def get_keys(self):
        keys = []
        for address in self.values:   # position  # with arrays, we would have looped through a few items only
            if address:
                for pair in address:  # with this: O(n^2), but this rarely happens with a large enough hash table  # TOCHECK: any benefits from checking if len(pair) > 1 and treat them differently?
                    keys.append(pair[0])
        return keys
            

    
hash_table = HashTable(3)

hash_table.set_value('lala', 1)
hash_table.set_value('lolo', 2)
hash_table.set_value('lele', 3)
hash_table.set_value('lele', 10)
hash_table.set_value('lili', 5)

print(hash_table.get_values())
# print(hash_table.get_value('lulu'))  # None
print(hash_table.get_value('lele'))
print(hash_table.get_value('lele'))
print(hash_table.get_value('lili'))
# print(hash_table.get_value('lele'))

print(hash_table.get_keys())
