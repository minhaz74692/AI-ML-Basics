class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr= [None for i in range(self.MAX)]

    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __setitem__(self, key, value):
        self.add(key, value)

    def get(self, key):
        h = self.get_hash(key)
        if h>= self.MAX:
            print("Invalid key")
            raise Exception("Invalid key")
        g = self.arr[h]
        if g:
            return g
        else:
            raise Exception("Not found")

    def __getitem__(self, key):
       return self.get(key)

    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    def __delitem__(self, key):
        self.delete(key)






if __name__ == "__main__":
    ht = HashTable()

    n = ht.get_hash("march 6")
    print(n)

    ht.add("march 6", 101)
    ht['march 7'] = 201 #this comes from __setitem__ (Which is a python standard operator)

    print(ht.arr)

    print("Get result: " ,ht.get("march 6"))
    print("Get item by python standard operator: ", ht["march 7"])

    ht.delete("march 6")
    del ht["march 7"] #this comes from __delitem__ (Which is a python standard operator)
    print(ht.arr)


