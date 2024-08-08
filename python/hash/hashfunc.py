my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
my_hash_set = [None,None,None,None,None,None,None,None,None,None]

def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10

# to handle collission, insert turn my_hash_set into n dimension array

for i in range(len(my_array)):
    hash_index = hash_function(my_array[i])
    bucket = []
    bucket.append(my_array[i])
    my_hash_set.insert(hash_index, bucket)


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

print(my_hash_set)
el = "Amae"
print(f"Contains: {el}:-> {contains(el)}")
