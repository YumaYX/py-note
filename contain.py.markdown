The Python code snippet `contain = pattern in text` checks whether the string `pattern` is present within the string `text`. If `pattern` is found in `text`, the variable `contain` will be set to `True`; otherwise, it will be `False`. This is a straightforward way to perform a substring search in Python.


## Code:

```python
#!/usr/bin/env python3

text = "this is text string"
pattern = "is text"

contain = pattern in text

print(contain)
```

## Output:

```
True
```

