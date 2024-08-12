from pprint import pprint

class Hashset:
    def __init__(self, size:int=20) -> None:
        self.size = size
        self.hashset = [[] for _ in range(size)]
        return
    
    def hash_function(self, element) -> int:
        unicode_sum = 0
        for char in str(element):
            unicode_sum += ord(char)
        hash_index = unicode_sum % self.size
        return hash_index

    def add(self, element) -> None:
        hash_index = self.hash_function(element)
        bucket = self.hashset[hash_index]
        if element not in bucket:
            bucket.append(element)
        return
    
    def remove(self, element):
        hash_index = self.hash_function(element)
        bucket = self.hashset[hash_index]
        if element in bucket:
            temp = element
            bucket.remove(element)
            return temp

        return f"{element} is not in hash setc"
    
    def contains(self, element) -> bool:
        hash_index = self.hash_function(element)
        return element in self.hashset[hash_index]
    
    def print_set(self):
        print("Has set Contents")
        for index, element in enumerate(self.hashset):
            print(f"{index + 1}:-> {element}")


testhash = Hashset(size=2)
testhash.add("Amaechi")
testhash.add(121)
print(f"Hashset contains 121:-> {testhash.contains(121)}\n")
testhash.print_set()
