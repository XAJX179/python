import os
with open('renam.txt') as f:
    text = f.read()

with open('my_renamed_file.txt','w') as f:
    f.write(text)

os.remove('renam.txt')