
```python3
l = [1, 2, 5, 2, 4]
rotations = [5, 6, 7, 8, 9]
max_elem = max(l)
max_idx = l.index(max_elem)

result = []
for rot in rotations:
    rot = rot % len(l)
    
    if rot == 0:
        result.append(max_idx)
    elif rot <= max_idx:
        result.append(max_idx - rot)
    elif rot > max_idx:
        rot = rot - max_idx
        result.append(len(l) - rot)
print(result)
```