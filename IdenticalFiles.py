with open('sample2.txt')as f:
    file1 = f.read()

with open('copy.txt')as f:
    file2 = f.read()

if file1 == file2:
    print("Files are identical.")
else:
    print("Files are NOT identical.")
