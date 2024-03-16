file = open('sample.txt')

x = file.readline()
print(x.strip(),end=' ')

x = file.readline()
print(x)

file.close()
