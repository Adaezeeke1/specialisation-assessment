# 3.1 Designing a hash function to convert a string into hash code within a certain range

def basic_hash_function(input_string, table_size):
    hash_value = 0
    for letter in input_string:
        hash_value += ord(letter)
    return hash_value % table_size

# In this function,
# - 'input_string' is the string I want to hash
# - 'table_size' is the size of the hash table/ number of buckets


# 3.2 No Hash Collision
# I will use the basic hash function to hash 2 different strings: 'apple' and 'banana', assuming a table size of 10.


table_size = 10

hashed_value_apple = basic_hash_function("apple", table_size)
hashed_value_banana = basic_hash_function("banana", table_size)

print("Hashed value for 'apple':", hashed_value_apple)
print("Hashed value for 'banana':", hashed_value_banana)

# To walkthrough, the characters of the string "apple" are converted to their ASCII values:
#
# 'a' -> 97
# 'p' -> 112
# 'p' -> 112
# 'l' -> 108
# 'e' -> 101
#
# Next, the ASCII values are added: 97 + 112 + 112 + 108 + 101 = 530.
#
# Next, it performs the modulo operation to fit the sum into the range of the table size:
# - 530 % 10 = 0.

# The hash value for "apple" is 0. This means it will be stored in bucket 0 of the hash table.
#
# The function then repeats the process for the string "banana":
#
# Converts ASCII values:
# 'b' -> 98
# 'a' -> 97,
# 'n' -> 110,
# 'a' -> 97,
# 'n' -> 110,
# 'a' -> 97.
#
# Sums the ASCII values: 98 + 97 + 110 + 97 + 110 + 97 = 609.
#
# Performs modulo operation: 609 % 10 = 9.
#
# The hash value for "banana" is 9. It will be stored in bucket 9 of the hash table.
#
# Result:
# Hashed value for "apple": 0 (bucket 0)
# Hashed value for "banana": 9 (bucket 9)
#
#
# 3.3 Hash Collision
# I will use the basic hash function to hash 2 different strings: 'dog' and 'god', again assuming a table size of 10.

hashed_value_dog = basic_hash_function("dog", table_size)
hashed_value_god = basic_hash_function("god", table_size)

print("Hashed value for 'dog':", hashed_value_dog)
print("Hashed value for 'god':", hashed_value_god)

# We'll use the strings "dog" and "god," along with a table size of 10.
#
# To walkthrough, the characters of the string "dog" are converted to their ASCII values:
#
# 'd' -> 100
# 'o' -> 111
# 'g' -> 103

# Next, the ASCII values are added: 100 + 111 + 103 = 314.
#
# Next, it performs the modulo operation to fit the sum into the range of the table size:
# - 314 % 10 = 4.
#
# The hash value for "dog" is 4. Thus, it will be stored in bucket 4 of the hash table.
#
# The function then repeats the process for the string "god":
#
# Converts ASCII values:
# 'g' -> 103
# 'o' -> 111
# 'd' -> 100.
#
# Sums the ASCII values: 103 + 111 + 100 = 314.
#
# Performs modulo operation: 314 % 10 = 4.
#
# The hash value for "god" is also 4. It will be stored in the same bucket 4 of the hash table, causing a collision.
#
# To handle the collision, we would maintain a linked list in bucket 4 of the hash table.
#
# The linked list would contain both "dog" and "god."
#
# Result:
# Hashed value for "dog": 4 (bucket 4, linked list: "dog", "god")
