n = int(input("Enter no. >= 3 :"))

for i in range(n):
    if i == 0:
        print("*"*n)
    if i == (n-1):
        print("*"*n)
    elif i>0 and i < n-1 :
        print('*',end='')
        print(" "*(n-2),end='')
        print('*')
        