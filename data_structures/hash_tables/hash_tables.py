"""
Create a hash table that allows getting and setting key-value pairs
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

    def set_value(self, key, value):
        hashed_key = hash(key) % self.size  # self.hash(key)  # TODO: compare with built-in hash()
        print("hashed_key: {}".format(hashed_key))
        # self.values.insert(hashed_key, value)
        (self.values)[hashed_key] = value

    def get_value(self, key):
        try:
            hashed_key = hash(key) % self.size  # self.hash(key)
            value = self.values[hashed_key]
            return value
        except:
            print("Key not in hash table")

    def get_values(self):
        return self.values

    
hash_table = HashTable(50)
print(hash_table.get_value('lala'))
hash_table.set_value('lala', 100)
print(hash_table.get_value('lala'))

print(hash_table.get_value('lolo'))
hash_table.set_value('lolo', 1000)
print(hash_table.get_value('lolo'))

print(hash_table.get_value('lele'))
hash_table.set_value('lele', 5000)
print(hash_table.get_value('lele'))
print(hash_table.get_value('lele'))
hash_table.set_value('lele', 3000)
print(hash_table.get_value('lele'))

print(hash_table.get_values())
