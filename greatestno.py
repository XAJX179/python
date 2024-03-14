# a1 = int(input("Enter No. :"))
# a2 = int(input("Enter No. :"))
# a3 = int(input("Enter No. :"))
# a4 = int(input("Enter No. :"))

# gn = {a1,a2,a3,a4}

# print(max(gn),"is the Greatest")

a1 = int(input("Enter No. :"))
a2 = int(input("Enter No. :"))
a3 = int(input("Enter No. :"))
a4 = int(input("Enter No. :"))

if a1 > a2:
    greatest = a1
else:
    greatest = a2

if a3 > a4:
    greatest2 = a3
else:
    greatest2 = a4

if(greatest2>greatest):
    print(str(greatest2)+" is greatest")
else:
    print(str(greatest)+" is greatest")

if(greatest!=0):
    pass