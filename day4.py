# whiteboard of the day
# Consecutive Indices
# You are given a list of unique integers (arr), and two integers (a and b). 
# Your task is to find out whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.
# Example:
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)
# Output: True
# Input: ([3,1,0,19], 19, 0)
# Output: True

# find index of n1 and n2
# if indexes are consecutive, return True
# if indexes are not conescutive, return False


def consecList(lst, n1, n2):
        if lst.index(n1) + 1 == lst.index(n2) or lst.index(n1) -1 == lst.index(n2):
            return True
        else:
            return False

# more efficient way of solving whiteboard
# def consecList(lst, n1, n2):
#     n1_i = lst.index(n1)
#     n2_i = lst.index(n2)

#     if n1_i + 1 == n2_i or n1_i == n2_i:
#         return True
#     else:
#         return False

print(consecList([3,1,0,19], 19, 0))
print(consecList([1, 6, 9, -3, 4, -78, 0], -3, 4))
print(consecList([3,1,0,19], 3, 19))

# notes on Time
# O(n) means linear
# O(1) means constant

count = 0
for i in range(5):
    for j in range(5):
        count += 1

print(count)

def removeVowel(string):
    output = '' # constant
    for letter in string: # linear
        if letter in {'a', 'e', 'i', 'o', 'u'}: # constant
            continue # constant
        else: # constant
            output += letter # constant
    return output

# notes on space complexity
