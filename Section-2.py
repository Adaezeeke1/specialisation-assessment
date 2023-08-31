def count_unique_consonants(x):
    consonants = set("bcdfghjklmnpqrstvwxyz")
    consonant_count = {}

    for character in x:
        if character.lower() in consonants:
            consonant_count[character.lower()] = consonant_count.get(character.lower(), 0) + 1

    unique_consonant_count = 0
    for count in consonant_count.values():
        if count == 1:
            unique_consonant_count += 1

    return unique_consonant_count


input1 = "cat"
input2 = "cataract"

output1 = count_unique_consonants(input1)
output2 = count_unique_consonants(input2)

print("EXAMPLE INPUT:", input1)
print("EXAMPLE OUTPUT:", output1)

print("EXAMPLE INPUT:", input2)
print("EXAMPLE OUTPUT:", output2)


# Time Complexity:
#
# - The loop that iterates through each character in the input string has a time complexity of O(n),
#   where n is the length of the input string.
#
# - Counting occurrences of consonants in the consonant_count dictionary takes O(1) on average
#   (due to dictionary operations).

# - The loop that counts the number of unique consonants also takes O(n) time in the worst case,
#   as we need to consider each entry in the consonant_count dictionary.
#
# Overall, the time complexity of the function is O(n), where n is the length of the input string.

# Space Complexity:
# The space complexity is determined by the additional data structures used:
#
# - The consonants set takes O(21) space (constant) since there are 21 lowercase consonant characters.
#
# - The consonant_count dictionary can store at most 21 entries (one for each consonant),
#   resulting in O(21) space as well.
#
# - Other variables used in the function take constant space.
#
# Hence, the space complexity of the function is O(1), as the space used does not grow with the input size.
#
# Assumption:
#
# This solution assumes that the input contains only alphabetical characters (letters) and does not include spaces,
# digits, or special characters.


def count_squares(x):
    if x == 1:
        return 1
    else:
        return x * x + count_squares(x - 1)


print("Number of squares in 1x1 grid:", count_squares(1))
print("Number of squares in 2x2 grid:", count_squares(2))
print("Number of squares in 3x3 grid:", count_squares(3))
