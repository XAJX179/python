names = ["darren",'Raj','''cody''','shub','sweetie']

name = str(input("Enter Name :"))

if name in names:
    print("hello my friend")
    print('at '+str(names.index(name)) +' in list')

else:
    print('who u small pp')
