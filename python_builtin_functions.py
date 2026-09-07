"""
NAME: Vandana Illipilla
TOPIC: Python Built-in Functions & Methods
"""

# ==========================================
# 1. STRING METHODS
# ==========================================
print("=" * 40)
print("1. STRING METHODS")
print("=" * 40)

# 1. lower(): Converts all characters in a string to lowercase
a = "HI"
print(f"lower(): {a.lower()}")  # Output: 'hi'

# 2. upper(): Converts all characters in a string to uppercase
b = "python"
print(f"upper(): {b.upper()}")  # Output: 'PYTHON'

# 3. capitalize(): Converts the first character to uppercase, rest to lowercase
c = "python programming"
print(f"capitalize(): {c.capitalize()}")  # Output: 'Python programming'

# 4. title(): Converts the first character of each word to uppercase
d = "python programming"
print(f"title(): {d.title()}")  # Output: 'Python Programming'

# 5. strip(): Removes leading and trailing whitespaces
e = " python "
print(f"strip(): '{e.strip()}'")  # Output: 'python'

# 6. replace(): Replaces a specified substring with another
f = "I like Java"
print(f"replace(): {f.replace('Java', 'Python')}")  # Output: 'I like Python'

# 7. split(): Splits a string into a list of substrings
g = "Python is easy"
print(f"split(): {g.split()}")  # Output: ['Python', 'is', 'easy']

# 8. find(): Returns index of first occurrence, or -1 if not found
h = "python"
print(f"find('t'): {h.find('t')}")  # Output: 2

# 9. count(): Returns count of occurrences of a substring
i = "python programming"
print(f"count('p'): {i.count('p')}")  # Output: 2

# 10. startswith(): Checks if string starts with specified prefix
j = "Python"
print(f"startswith('Py'): {j.startswith('Py')}")  # Output: True

# 11. endswith(): Checks if string ends with specified suffix
k = "Python"
print(f"endswith('on'): {k.endswith('on')}")  # Output: True

# 12. isdigit(): Checks if all characters are digits
l = "12345"
print(f"isdigit(): {l.isdigit()}")  # Output: True

# 13. isalpha(): Checks if all characters are alphabets
m = "Python"
print(f"isalpha(): {m.isalpha()}")  # Output: True

# 14. join(): Combines elements of an iterable with a separator
n = ["Python", "AI"]
print(f"join(): {'-'.join(n)}")  # Output: 'Python-AI'


# ==========================================
# 2. LIST METHODS
# ==========================================
print("\n" + "=" * 40)
print("2. LIST METHODS")
print("=" * 40)

# A List is an ordered, mutable collection allowing duplicate values.
lst = ["ML", "DS", "AI", "Python"]
print(f"Original List: {lst}")

# 1. append(): Adds 1 item at the end
a = ["ML", "DS"]
a.append("AI")
print(f"append('AI'): {a}")  # Output: ['ML', 'DS', 'AI']

# 2. insert(): Adds an element at a particular index
a = ["ML", "DS"]
a.insert(1, "AI")
print(f"insert(1, 'AI'): {a}")  # Output: ['ML', 'AI', 'DS']

# 3. remove(): Deletes an element by value
a = ["ML", "DS", "AI"]
a.remove("DS")
print(f"remove('DS'): {a}")  # Output: ['ML', 'AI']

# 4. pop(): Deletes an element by index (or last if index not specified)
a = ["ML", "DS", "AI"]
popped = a.pop()
print(f"pop(): {a} (removed: {popped})")  # Output: ['ML', 'DS']

# 5. sort(): Arranges elements in ascending order
a = [30, 10, 20]
a.sort()
print(f"sort(): {a}")  # Output: [10, 20, 30]

# 6. reverse(): Reverses the order of list elements
a = [1, 2, 3]
a.reverse()
print(f"reverse(): {a}")  # Output: [3, 2, 1]

# 7. count(): Returns occurrences of a value
a = [1, 2, 2, 3]
print(f"count(2): {a.count(2)}")  # Output: 2

# 8. index(): Returns index position of first occurrence
a = ["ML", "DS", "AI"]
print(f"index('DS'): {a.index('DS')}")  # Output: 1

# 9. extend(): Merges another iterable to the list
a = ["ML", "DS"]
b = ["AI", "Python"]
a.extend(b)
print(f"extend(b): {a}")  # Output: ['ML', 'DS', 'AI', 'Python']

# 10. clear(): Removes all elements from the list
a = ["ML", "DS", "AI"]
a.clear()
print(f"clear(): {a}")  # Output: []


# ==========================================
# 3. TUPLE METHODS
# ==========================================
print("\n" + "=" * 40)
print("3. TUPLE METHODS")
print("=" * 40)

# A Tuple is an ordered, immutable collection allowing duplicates.
numbers = (10, 20, 30)
print(f"Tuple: {numbers}")

# 1. count(): Counts occurrences of a value
numbers_tuple = (1, 2, 2, 3)
print(f"count(2): {numbers_tuple.count(2)}")  # Output: 2

# 2. index(): Returns position of an element
numbers_tuple = (10, 20, 30)
print(f"index(20): {numbers_tuple.index(20)}")  # Output: 1


# ==========================================
# 4. SET METHODS
# ==========================================
print("\n" + "=" * 40)
print("4. SET METHODS")
print("=" * 40)

# A Set is an unordered collection of unique values (no duplicates).
numbers_set = {1, 2, 2, 3, 4}
print(f"Set (duplicates removed): {numbers_set}")  # Output: {1, 2, 3, 4}

# 1. add(): Adds one element
s = {1, 2}
s.add(3)
print(f"add(3): {s}")  # Output: {1, 2, 3}

# 2. update(): Adds multiple elements
s = {1, 2}
s.update([3, 4])
print(f"update([3, 4]): {s}")  # Output: {1, 2, 3, 4}

# 3. remove(): Removes an element (raises KeyError if not found)
s = {1, 2, 3}
s.remove(2)
print(f"remove(2): {s}")  # Output: {1, 3}

# 4. discard(): Removes an element without raising error if absent
s = {1, 2, 3}
s.discard(5)
print(f"discard(5): {s}")  # Output: {1, 2, 3}

# 5. pop(): Removes and returns a random element
s = {10, 20, 30}
popped_val = s.pop()
print(f"pop(): {s} (removed: {popped_val})")

# 6. clear(): Removes all elements
s = {1, 2, 3}
s.clear()
print(f"clear(): {s}")  # Output: set()


# ==========================================
# 5. DICTIONARY METHODS
# ==========================================
print("\n" + "=" * 40)
print("5. DICTIONARY METHODS")
print("=" * 40)

# A Dictionary stores data as key-value pairs with unique keys.
student = {
    "name": "Vandana",
    "age": 22
}
print(f"Dictionary: {student}")

# 1. keys(): Returns a view of all keys
print(f"keys(): {student.keys()}")

# 2. values(): Returns a view of all values
print(f"values(): {student.values()}")

# 3. items(): Returns key-value pairs as tuples
print(f"items(): {student.items()}")

# 4. get(): Safely retrieves value of a key
print(f"get('name'): {student.get('name')}")  # Output: Vandana

# 5. update(): Updates or adds key-value pairs
student_sample = {"name": "Vandana"}
student_sample.update({"age": 22})
print(f"update({{'age': 22}}): {student_sample}")

# 6. pop(): Removes a key and returns its value
student_sample = {"name": "Vandana", "age": 22}
student_sample.pop("age")
print(f"pop('age'): {student_sample}")

# 7. popitem(): Removes and returns the last inserted key-value pair
student_sample = {"name": "Vandana", "age": 22}
item = student_sample.popitem()
print(f"popitem(): {student_sample} (popped: {item})")

# 8. copy(): Creates a shallow copy
student_sample = {"name": "Vandana"}
new_student = student_sample.copy()
print(f"copy(): {new_student}")

# 9. clear(): Removes all key-value pairs
student_sample = {"name": "Vandana", "age": 22}
student_sample.clear()
print(f"clear(): {student_sample}")  # Output: {}


# ==========================================
# 6. FILE HANDLING METHODS
# ==========================================
print("\n" + "=" * 40)
print("6. FILE HANDLING METHODS")
print("=" * 40)

# 1. open() & write()
with open("sample.txt", "w") as f:
    f.write("Python")
print("Written 'Python' to sample.txt")

with open("data.txt", "w") as f:
    f.write("Python Programming\nJava\nSQL")
print("Written lines to data.txt")

# 2. read(): Reads complete file content
with open("data.txt", "r") as f:
    content = f.read()
    print(f"read():\n{content}")

# 3. readline(): Reads one line at a time
with open("data.txt", "r") as f:
    line1 = f.readline().strip()
    print(f"readline(): {line1}")

# 4. readlines(): Reads all lines and returns a list
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(f"readlines(): {lines}")

# 5. tell() and seek(): Track and move file pointer
with open("data.txt", "r") as f:
    pos0 = f.tell()
    f.seek(7)
    seek_read = f.read()
    print(f"tell() start position: {pos0}")
    print(f"seek(7) read remainder: '{seek_read}'")


# ==========================================
# 7. JSON METHODS
# ==========================================
print("\n" + "=" * 40)
print("7. JSON METHODS")
print("=" * 40)

import json

# 1. json.dumps(): Converts Python object -> JSON string
data_obj = {"name": "Vandana", "age": 22}
json_str = json.dumps(data_obj)
print(f"json.dumps(): {json_str} (Type: {type(json_str).__name__})")

# 2. json.loads(): Converts JSON string -> Python object
json_input = '{"name": "Vandana"}'
parsed_obj = json.loads(json_input)
print(f"json.loads(): {parsed_obj} (Type: {type(parsed_obj).__name__})")

# 3. json.dump(): Writes JSON data directly to a file
with open("data.json", "w") as f:
    json.dump({"name": "Python"}, f)
print("json.dump(): saved to data.json")

# 4. json.load(): Reads JSON data directly from a file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(f"json.load(): {loaded_data}")

print("\nAll Python functions executed successfully!")
