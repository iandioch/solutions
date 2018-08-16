An implementation and string formatting problem. Annoying.

Worth remembering the python shorthand for rotating a list 90 degrees:

```python
def rotate(g):
    return list(zip(*g[::-1]))
```

This solution runs in 0.02s in python3.
