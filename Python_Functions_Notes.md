# Python Built-in Functions & Methods

**Author:** Vandana Illipilla  

---

## 1. String Methods

| Method | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| `lower()` | Converts all characters in a string to lowercase | `a = "HI"; a.lower()` | `'hi'` |
| `upper()` | Converts all characters in a string to uppercase | `b = "python"; b.upper()` | `'PYTHON'` |
| `capitalize()` | Converts first character to uppercase, rest to lowercase | `c = "python programming"; c.capitalize()` | `'Python programming'` |
| `title()` | Converts first character of each word to uppercase | `d = "python programming"; d.title()` | `'Python Programming'` |
| `strip()` | Removes spaces from beginning and end of string | `e = " python "; e.strip()` | `'python'` |
| `replace()` | Replaces specified character or word with another | `f = "I like Java"; f.replace("Java", "Python")` | `'I like Python'` |
| `split()` | Splits string into a list of substrings | `g = "Python is easy"; g.split()` | `['Python', 'is', 'easy']` |
| `find()` | Returns index position of first occurrence (or -1) | `h = "python"; h.find("t")` | `2` |
| `count()` | Returns number of times a specified value appears | `i = "python programming"; i.count("p")` | `2` |
| `startswith()`| Checks whether a string starts with a specified value | `j = "Python"; j.startswith("Py")` | `True` |
| `endswith()` | Checks whether a string ends with a specified value | `k = "Python"; k.endswith("on")` | `True` |
| `isdigit()` | Checks whether all characters in string are digits | `l = "12345"; l.isdigit()` | `True` |
| `isalpha()` | Checks whether all characters in string are alphabets | `m = "Python"; m.isalpha()` | `True` |
| `join()` | Combines elements of a list into string using separator | `n = ["Python", "AI"]; "-".join(n)` | `'Python-AI'` |

---

## 2. List Methods (`[]`)

A **List** is an ordered, mutable collection that allows duplicate values.

```python
a = ["ML", "DS", "AI", "Python"]
```

| Method | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| `append()` | Adds 1 item at the end | `a.append("AI")` | `['ML', 'DS', 'AI']` |
| `insert()` | Adds element at a particular index | `a.insert(1, "AI")` | `['ML', 'AI', 'DS']` |
| `remove()` | Deletes element by its value | `a.remove("DS")` | `['ML', 'AI']` |
| `pop()` | Deletes element by its index | `a.pop()` | `['ML', 'DS']` |
| `sort()` | Arranges elements alphabetically or numerically | `a = [30, 10, 20]; a.sort()` | `[10, 20, 30]` |
| `reverse()`| Displays elements in reverse order | `a = [1, 2, 3]; a.reverse()` | `[3, 2, 1]` |
| `count()` | Finds number of occurrences | `a = [1, 2, 2, 3]; a.count(2)` | `2` |
| `index()` | Finds position of an element | `a.index("DS")` | `1` |
| `extend()` | Merges two lists | `a.extend(["AI", "Python"])` | `['ML', 'DS', 'AI', 'Python']` |
| `clear()` | Makes the list empty | `a.clear()` | `[]` |

---

## 3. Tuple Methods (`()`)

A **Tuple** is an ordered, immutable collection that allows duplicates.

| Method | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| `count()` | Counts occurrences | `(1, 2, 2, 3).count(2)` | `2` |
| `index()` | Returns position of an element | `(10, 20, 30).index(20)` | `1` |

---

## 4. Set Methods (`{}`)

A **Set** is an unordered collection of unique values (no duplicates).

| Method | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| `add()` | Adds one element | `{1, 2}.add(3)` | `{1, 2, 3}` |
| `update()` | Adds multiple elements | `{1, 2}.update([3, 4])` | `{1, 2, 3, 4}` |
| `remove()` | Removes an element (error if not found) | `{1, 2, 3}.remove(2)` | `{1, 3}` |
| `discard()`| Removes element without raising error if missing | `{1, 2, 3}.discard(5)` | `{1, 2, 3}` |
| `pop()` | Removes a random element | `{10, 20, 30}.pop()` | Element removed |
| `clear()` | Removes all elements | `{1, 2, 3}.clear()` | `set()` |

---

## 5. Dictionary Methods (`{}`)

A **Dictionary** stores data as key-value pairs where keys are unique.

```python
student = {"name": "Vandana", "age": 22}
```

| Method | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| `keys()` | Returns all keys | `student.keys()` | `dict_keys(['name', 'age'])` |
| `values()` | Returns all values | `student.values()` | `dict_values(['Vandana', 22])` |
| `items()` | Returns key-value pairs | `student.items()` | `dict_items([('name', 'Vandana'), ('age', 22)])` |
| `get()` | Gets value of a key safely | `student.get("name")` | `'Vandana'` |
| `update()` | Updates or adds key-value pairs | `student.update({"age": 22})`| `{'name': 'Vandana', 'age': 22}` |
| `pop()` | Removes a key | `student.pop("age")` | `{'name': 'Vandana'}` |
| `popitem()`| Removes last inserted key-value pair | `student.popitem()` | `('age', 22)` |
| `copy()` | Creates a copy of the dictionary | `student.copy()` | `{'name': 'Vandana'}` |
| `clear()` | Removes all key-value pairs | `student.clear()` | `{}` |

---

## 6. File Handling in Python

Used to create, read, write, and modify files.

### Modes:
- `r` &rarr; Read
- `w` &rarr; Write
- `a` &rarr; Append
- `x` &rarr; Create new file

| Function / Method | Description | Example |
| :--- | :--- | :--- |
| `open()` | Opens a file | `f = open("sample.txt", "w")` |
| `write()` | Writes data into a file | `f.write("Python Programming")` |
| `read()` | Reads complete file content | `f.read()` |
| `readline()` | Reads one line at a time | `f.readline()` |
| `readlines()` | Reads all lines and returns a list | `f.readlines()` |
| `tell()` | Returns current file pointer position | `f.tell()` |
| `seek()` | Moves file pointer to a position | `f.seek(5)` |
| `close()` | Closes the file | `f.close()` |

---

## 7. JSON Methods in Python

```python
import json
```

| Method | Purpose | Example |
| :--- | :--- | :--- |
| `json.dumps()` | Converts Python object &rarr; JSON string | `json.dumps({"name": "Vandana"})` |
| `json.loads()` | Converts JSON string &rarr; Python object | `json.loads('{"name": "Vandana"}')` |
| `json.dump()` | Writes JSON data into a file | `json.dump(data, open("data.json", "w"))` |
| `json.load()` | Reads JSON data from a file | `json.load(open("data.json", "r"))` |

---

## 8. Python Key Differences

1. **`find()` vs `index()`**: `find()` returns `-1` if substring is not found, while `index()` raises `ValueError`.
2. **`append()` vs `extend()`**: `append()` adds 1 element/object as a whole, while `extend()` iterates and adds multiple elements.
3. **`remove()` vs `pop()`**: `remove()` removes by value (returns nothing), while `pop()` removes by index (returns the removed value).
4. **`List` vs `Tuple`**: List is mutable `[]`, Tuple is immutable `()`.
5. **`List` vs `Set`**: List maintains order & allows duplicates `[]`, Set has no duplicate values `{}`.
6. **`Dictionary` vs `Set`**: Dictionary stores key-value pairs, Set stores only unique values.
7. **`remove()` vs `discard()` (Set)**: `remove()` throws `KeyError` if element is not found, `discard()` does not raise an error.
8. **`==` vs `!=`**: `==` checks if values are equal, `!=` checks if values are not equal.
9. **`==` vs `is`**: `==` compares values/equality, `is` checks memory address/identity.
10. **`sort()` vs `sorted()`**: `sort()` modifies original list in-place, `sorted()` returns a new sorted list.
11. **`read()` vs `readline()` vs `readlines()`**:
    - `read()`: reads entire file content as a string.
    - `readline()`: reads one line as a string.
    - `readlines()`: reads all lines and returns a list of strings.
12. **`dump()` vs `dumps()`**: `dump()` writes to a file, `dumps()` returns a JSON string.
13. **`load()` vs `loads()`**: `load()` reads from a file, `loads()` parses from a string.
14. **`insert()` vs `Slicing`**: `insert()` inserts a single element, slicing can insert/replace multiple elements at once (`a[1:1] = [2, 3]`).
15. **`isdigit()` vs `isnumeric()`**: `isdigit()` checks digits (0-9), `isnumeric()` also includes numeric characters like fractions (`½`) and subscripts/superscripts.
16. **`break` vs `continue`**: `break` terminates the entire loop, `continue` skips the current iteration and moves to the next.
