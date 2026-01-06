class ChainingHashTable:
    def __init__(self):
        self.MAX = 100
        self.arr= [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        found =False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value) # This is for replacing value if the key already exist in the chain
                found = True
                break

        if not found:
            self.arr[h].append((key, value))





    def __setitem__(self, key, value):
        self.add(key, value)

    def get(self, key):
        h = self.get_hash(key)
        if h>= self.MAX:
            print("Invalid key")
            raise Exception("Invalid key")

        items = self.arr[h]
        if items and len(items)>0:
            for inx, item in enumerate(items):
                if item[0] == key:
                    return item[1]
        return None

    def __getitem__(self, key):
       return self.get(key)

    def delete(self, key):
        h = self.get_hash(key)

        items = self.arr[h]
        if items and len(items)>0:
            for idx, item in enumerate(items):
                if item[0] == key:
                    del self.arr[h][idx]


    def __delitem__(self, key):
        self.delete(key)






if __name__ == "__main__":
    ht = ChainingHashTable()

    n = ht.get_hash("march 6")
    print(n)

    ht.add("march 6", 101)
    ht.add("narch 5", 107)
    # ht["march 6"] = 102
    ht.add("march 17", 103)

    # ht['march 7'] = 201 #this comes from __setitem__ (Which is a python standard operator)

    print(ht.arr)

    ht.delete("march 6")

    print("Get result after delete 1: " ,ht.get("march 6"))
    print("Get result: " ,ht.get("narch 5"))
    print("Get item by python standard operator: ", ht["march 17"])

    ht.delete("march 6")
    del ht["march 7"] #this comes from __delitem__ (Which is a python standard operator)
    print("Get item by python standard operator after delete: ", ht["march 7"])


