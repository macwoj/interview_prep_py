# interview_prep_py

# for
```python
for k in f:
  if f[k] > char_freq[k]:
    break
else:
  # executes if break was NOT called
  result += len(w)
```

# Collections

## defaultdict
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

## set, hashtable

- issubset() method returns True if set A is the subset of B

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# all items of A are present in B
print(A.issubset(B))

# Output: True
```

## defaultdict, O(1)
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
