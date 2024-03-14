num = int(input("Enter No : (ノಠ益ಠ)ノ彡┻━┻  :"))

prime = True

for i in range(2, num):
    if (num % i == 0):
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Not Prime")
