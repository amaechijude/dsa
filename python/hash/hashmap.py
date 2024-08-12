class HashMap:
    def __init__(self, size=20) -> None:
        self.size = size
        self.bucket = [[] for _ in range(size)]

    def hash_function(self, key) -> int:
        sum_of_n = 0
        for char in str(key):
            n = ord(char)
            sum_of_n += n
        return int(sum_of_n % self.size)

    def put(self, key,value) -> None:
        hash_index = self.hash_function(key)
        bucket = self.bucket[hash_index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) #update the key value
                return
        bucket.append((key,value))
        return

    def get_key_value(self, key):
        hash_index = self.hash_function(key)
        bucket = self.bucket[hash_index]

        for k,v in bucket:
            if k == key:
                return v
        return 'key does not exist'

    def remove(self, key):
        hash_index = self.hash_function(key)
        bucket = self.bucket[hash_index]

        for k in bucket:
            if k[0] == key:
                bucket.remove(k)
                return k
        return "key does'nt exist"



    def print_v(self) -> list:
        return self.bucket


from pprint import pprint

hash_test = HashMap(10)
pprint(hash_test.print_v())
print(' ')
print(' ')

hash_test.put("Amaechi", "Python")
hash_test.put("jude", "git")
pprint(hash_test.print_v())
print(' ')
print(' ')

hash_test.put("lawn", "here")
hash_test.put("uni", "UNN")
pprint(hash_test.print_v())

print(f"\n\nRemoved:-> {hash_test.remove('lawn')}")
print(f"Removed:-> {hash_test.remove('haha')}")
print(f"Removed:-> {hash_test.remove(23)}\n\n")

hash_test.put("uni", "WellaHealth")
pprint(hash_test.print_v())
