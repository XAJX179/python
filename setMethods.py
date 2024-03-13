b = set()
b.add(2)
b.add(3)
b.add(3)
b.add(3)
b.add((2, 3, 5, 6))  # no list or dict
print(len(b))
print(b)


b.remove(2)
print(b)


b.pop()
print(b)


b = b.union({12, 23})
print(b)


b.clear()
print(b)
