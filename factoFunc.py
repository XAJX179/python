#for recursive
#n! = 1*2*3*4*...*n
#n! = 1*2*3*4*... *n-1 *n
#n! = (n-1)!*n
#4! = 1*2*3*4
#3! = 1*2*3
#4! = 3!*4

def factfunc(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return print(sum)

factfunc(int(input("Enter No.  ⤜(ⱺ ʖ̯ⱺ)⤏  : ")))

def factorecursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorecursive(n-1)

print(factorecursive(int(input("Enter a no.  ⤜(ⱺ ʖ̯ⱺ)⤏ :"))))

# def hell():
#     print("hello world!")
#     return hell()
# hell() 
#bad recursion example