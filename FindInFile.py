with open('sample.txt','r') as f:
    x = str(f.read())

y= x.find('Bell')

if y == -1:
    print('Not Present')
else:
    print(f"Present at index {y}")
