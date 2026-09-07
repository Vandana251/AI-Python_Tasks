"""
NAME: Vandana Illipilla
TOPIC: Key Differences in Python Concepts
"""

import json

print("=" * 60)
print("PYTHON KEY DIFFERENCES & COMPARISONS")
print("=" * 60)

# 1. find() vs index()
print("\n1. find() vs index()")
# find() returns -1 if substring is not found.
# index() raises a ValueError if substring is not found.
text = "python"
print("find('z'):", text.find("z"))  # Output: -1
try:
    print(text.index("z"))
except ValueError as e:
    print(f"index('z') raises ValueError: {e}")

# 2. append() vs extend()
print("\n2. append() vs extend()")
# append() adds single element (even if it's a list) at the end.
# extend() merges elements of iterable individually.
a1 = [1, 2]
a1.append([3, 4])
print("append([3, 4]):", a1)  # [1, 2, [3, 4]]

a2 = [1, 2]
a2.extend([3, 4])
print("extend([3, 4]):", a2)  # [1, 2, 3, 4]

# 3. remove() vs pop()
print("\n3. remove() vs pop()")
# remove() deletes element by value and returns nothing.
# pop() deletes element by index and returns the removed value.
l1 = [10, 20, 30]
l1.remove(20)
print("remove(20):", l1)  # [10, 30]

l2 = [10, 20, 30]
val = l2.pop(1)
print(f"pop(1): {l2}, popped value: {val}")  # [10, 30], 20

# 4. List vs Tuple
print("\n4. List vs Tuple")
# List is mutable (uses []), Tuple is immutable (uses ()).
lst = [1, 2]
lst.append(3)
print("List (mutable):", lst)
tup = (1, 2)
print("Tuple (immutable):", tup)
try:
    tup[0] = 5  # TypeError
except TypeError as e:
    print("Tuple modification raises TypeError:", e)

# 5. List vs Set
print("\n5. List vs Set")
# List allows duplicates and maintains order ([]).
# Set removes duplicates and has no guaranteed order ({}).
l = [1, 2, 2, 3]
s = {1, 2, 2, 3}
print("List with duplicates:", l)  # [1, 2, 2, 3]
print("Set unique elements:", s)    # {1, 2, 3}

# 6. Dictionary vs Set
print("\n6. Dictionary vs Set")
# Dictionary stores key-value pairs (uses keys to access values).
# Set stores unique values only.
d = {"name": "Ram", "age": 20}
st = {"Ram", 20}
print("Dictionary:", d)
print("Set:", st)

# 7. remove() vs discard() (Set)
print("\n7. remove() vs discard() in Set")
# remove() raises KeyError if element is not found.
# discard() does NOT raise an error if element is missing.
s = {1, 2, 3}
s.discard(5)
print("discard(5) (no error):", s)
try:
    s.remove(5)
except KeyError as e:
    print(f"remove(5) raises KeyError: {e}")

# 8. == vs !=
print("\n8. == vs !=")
a, b = 10, 10
print("10 == 10:", a == b)  # True
print("10 != 10:", a != b)  # False

# 9. == vs is
print("\n9. == vs is")
# == checks values equality.
# is checks memory location (identity).
list1 = [1, 2]
list2 = [1, 2]
print("list1 == list2 (values equal):", list1 == list2)  # True
print("list1 is list2 (different objects):", list1 is list2)  # False

# 10. sort() vs sorted()
print("\n10. sort() vs sorted()")
# sort() modifies the original list in-place and returns None.
# sorted() returns a new sorted list leaving original unchanged.
arr1 = [3, 1, 2]
arr1.sort()
print("sort() in-place:", arr1)

arr2 = [3, 1, 2]
new_arr = sorted(arr2)
print("sorted() new list:", new_arr, "| Original:", arr2)

# 11. dump() vs dumps() (JSON)
print("\n11. json.dump() vs json.dumps()")
# dump() writes to file object.
# dumps() serializes to JSON string.
data = {"name": "Python"}
json_str = json.dumps(data)
print("dumps() output string:", json_str)

# 12. load() vs loads() (JSON)
print("\n12. json.load() vs json.loads()")
# loads() parses JSON string.
# load() reads and parses from file object.
obj = json.loads('{"a": 1}')
print("loads() output dict:", obj)

# 13. insert() vs Slicing
print("\n13. insert() vs Slicing")
# insert() inserts a single element at an index.
# slicing can insert or replace multiple elements at once.
x = [1, 3]
x.insert(1, 2)
print("insert(1, 2):", x)  # [1, 2, 3]

y = [1, 4]
y[1:1] = [2, 3]
print("slicing y[1:1] = [2, 3]:", y)  # [1, 2, 3, 4]

# 14. isdigit() vs isnumeric()
print("\n14. isdigit() vs isnumeric()")
# isdigit() checks standard digit characters.
# isnumeric() supports numeric symbols, superscripts, fractions (e.g., ½).
digit_str = "123"
fraction_str = "½"
print("'123'.isdigit():", digit_str.isdigit(), "| '123'.isnumeric():", digit_str.isnumeric())
print("'½'.isdigit():", fraction_str.isdigit(), "| '½'.isnumeric():", fraction_str.isnumeric())

# 15. break vs continue
print("\n15. break vs continue")
print("Loop with break at 3:")
for num in range(5):
    if num == 3:
        break
    print(num, end=" ")
print("\nLoop with continue at 3:")
for num in range(5):
    if num == 3:
        continue
    print(num, end=" ")
print()
