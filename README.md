# interview_prep_py

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
