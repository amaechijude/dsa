from pprint import pprint


my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
my_hash_set = my_hash_set = []
for _ in range(11):
    my_hash_set.append([])

def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10

# to handle collission, turn my_hash_set into n dimension array

for i in range(len(my_array)):
    hash_index = hash_function(my_array[i])
    bucket = my_hash_set[hash_index]
    if my_array[i] not in bucket:
        bucket.append(my_array[i])


def add(param="Stuart"):
    hash_index = hash_function(param)
    bucket = my_hash_set[hash_index]
    if not bucket:
        bucket = [param]
        my_hash_set.insert(hash_index, bucket)
    else:
        if param not in bucket:
            bucket.append(param)
        
def contains(elemnt) -> bool:
    hash_index = hash_function(elemnt)
    return elemnt in my_hash_set[hash_index]



print(my_hash_set)
add()
add("Jones")
add("Amaechi")
add("Amaechi")
add("Maths")
add("Csharp")
add("Python")

print(my_hash_set)
el = "Amaechi"
print(f"Contains: {el}:-> {contains(el)}")
pprint(my_hash_set)
