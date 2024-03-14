names = ["darren",'Raj','''cody''','shub','sweetie']

name = str(input("Enter Name :"))

if name in names:
    print("hello my friend")
else:
    print('who u small pp')

print('at '+str(names.index(name)) +' in list')