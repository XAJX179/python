name = 'xX AJ xX'
print(len(name))
print(name.endswith('X'))
print(name.count('X'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find('AJ'))
print(name.replace('AJ','XAJX'))


#finding  name twice

name= 'So heres the string XAJX u like it? XAJX'

index = 0

while index <= len(name):
    index = name.find('XAJX',index)#starts search from this index next
    if index == -1:
        break
    print(index)
    index += 4