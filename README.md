# interview_prep_py

# variants
- [Random Pick Index](./exercises/398_rand_pick.py)
- [Random pick weight](./exercises/528_rand_pick_weight.py)
- [Range Sum of BST](./exercises/938_range_bst.py)
- [Max swap](./exercises/670_max_swap.py)
- [Accounts merge](./exercises/721_accouts_merge.py)
- [Calculator](./exercises/227_calculator.py)
- [BST range sum](./exercises/938_range_bst.py)
- [Next Perm](./exercises/31_next_perm.py)
- [First last element](./exercises/34_first_last_sorted.py)
- [Valid number](./exercises/65_valid_num.py)

# string
```python
"hello123".isalnum()    # True
"hello 123".isalnum()   # False (space)
"123!".isalnum()        # False (!)
"".isalnum()            # False (empty string)

s.isalpha() # only letters
s.isdigit() # only digits
s.isnumeric() # numeric (including Unicode numerals)
```

# class
```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = value
```

# for
```python
for k in f:
  if f[k] > char_freq[k]:
    break
else:
  # executes if break was NOT called
  result += len(w)
```
```python
# reverse range
count = [0, 1, 2, 3, 4, 5]
for c in range(len(count)-1, -1, -1):
    print(count[c])
```

# Collections

## list - slicing [start:end:step], end is NOT included as an index, start IS included as an index
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(my_list[2:5])  # Output: [2, 3, 4]

# Slicing with step
print(my_list[1:8:2]) # Output: [1, 3, 5, 7]

# Slicing from start
print(my_list[:5])  # Output: [0, 1, 2, 3, 4]

# Slicing to end
print(my_list[5:])  # Output: [5, 6, 7, 8, 9]

# Slicing with negative indices
print(my_list[-3:-1])  # Output: [7, 8]

# Reverse slicing
print(my_list[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### sort
```python
numbers = [5, 2, 9, 1]
numbers.sort(key=lambda x: -x)  # Sort descending using key
print(numbers)  # [9, 5, 2, 1]
```

```python
pairs = [(1, 3), (2, 2), (3, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(3, 1), (2, 2), (1, 3)]
```

## stack
```python
stack = []

# add to back
stack.append('a')

# remove and return form back
stack.pop()
```
## dict open addressing with quadratic probing

### defaultdict
``` python
from collections import defaultdict

# Create a defaultdict with a default
# value of an empty list
d = defaultdict(list)

# Add elements to the defaultdict and print it
d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)

# No key error raised here and an empty list
# is printed
print(d['juices'])
```

```python
from collections import OrderedDict

my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move key 'a' to the end
my_dict.move_to_end('a')

# Move key 'b' to the beginning
my_dict.move_to_end('b', last=False)

last_item = my_dict.popitem(last=True)

for key, value in od.items():
    print(key, value)
```

### set, hashtable

- issubset() method returns True if set A is the subset of B

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# all items of A are present in B
print(A.issubset(B))

# Output: True
```

## deque
```python
from collections import deque

dq = deque([10, 20, 30])

# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  
```

## heap (min heap)
```python
import heapq

# Create a heap from a list
heap = [5, 3, 8, 1, 2]
# O(n)
heapq.heapify(heap)
print(heap)  # Now it's a valid heap (min-heap)

# Add an element
# O(log n)
heapq.heappush(heap, 0)
print(heap)

# Remove and return the smallest element
# O(log n)
smallest = heapq.heappop(heap)
print(smallest)
print(heap)

# Peek at the smallest element without popping
# O(1)
print(heap[0])
```

# Algorithms

## Binary search
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]<=target:
            lo=mid+1
        else:
            hi=mid-1
    return lo
```

- `binary_search([1,2,3,4],5)` -> 4 (bigger than largest, one past the last element)
- `binary_search([1,2,3,4],0)` -> 0 (less than smallest, first element)
- `binary_search([1, 2, 6, 7],5)` -> 2 (insertion index is element that is bigger)
- `binary_search([1, 2, 6, 7],3)` -> 2 (insertion index is element that is bigger)
- `binary_search([1, 2, 6, 7],2)` -> 2 (equals, insertion is next element not equal)
- `binary_search([1, 2, 6, 7, 7, 7, 7, 8, 9, 10, 11],7)` -> 7 (equals, insertion is next element not equal)


## LRU Cache
```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)
```

# file manipulation

### 1. **Read from a File**
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```
### 2. **Write to a File (Overwrite)**
```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
```
### 3. **Append to a File**
```python
with open('example.txt', 'a') as file:
    file.write("Appended line.\n")
```
### 4. **Read File Line by Line**
```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```
### 🗃️ 5. **Copy a File**
```python
import shutil

shutil.copy('example.txt', 'copy_example.txt')
```
### 6. **Rename or Move a File**
```python
import os

os.rename('copy_example.txt', 'renamed_example.txt')
```
### 7. **Delete a File**
```python
import os

if os.path.exists('renamed_example.txt'):
    os.remove('renamed_example.txt')
```
### 8. **List Files in a Directory**
```python
import os

for filename in os.listdir('.'):
    print(filename)
```
### 9. **Check if File Exists**
```python
import os

if os.path.isfile('example.txt'):
    print("File exists.")
```
