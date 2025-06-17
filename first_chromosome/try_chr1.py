# Try

# seq = "asdfghjkl"
# print(seq[-4:])


# --=-
from itertools import permutations

# Define your set of items (can be numbers, strings, etc.)
items = ['A', 'B', 'C', 'D']  # Example with 4 items

# Generate all permutations of length 3
perms = permutations(["A", "T", "G", "C"], 3)

# Convert the iterator to a list to view all permutations
perm_list = list(perms)

# Print the result
print(f"Total permutations: {len(perm_list)}")
for p in perm_list:
    print(p)
