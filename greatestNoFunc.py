n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

def great(a1,a2,a3):
    greatest=0
    if a1 >= a2 and a1>=a3:
        return a1
    elif  a2 >= a1 and a2>=a3:
        return a2
    elif a3 >= a1 and a3>=a2:
        return a3

greatest= great(n1,n2,n3)

print(f"{greatest} is the greatest!  ʕノ•ᴥ•ʔノ ︵ ┻━┻  ")