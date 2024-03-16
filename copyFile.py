with open('sample2.txt') as f:
    text = f.read()

with open('copy.txt', 'w') as f:
    f.write(text)