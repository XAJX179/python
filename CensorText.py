with open('sample.txt') as f:
   content = f.read()

content = content.replace('Donkey','#%$#$$')

with open('sample.txt','w') as f:
    f.write(content)