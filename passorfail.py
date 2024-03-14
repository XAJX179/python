a1 = int(input("Enter Marks for 1 => ?/80 :"))
a2 = int(input("Enter Marks for 2 => ?/80 :"))
a3 = int(input("Enter Marks for 3 => ?/80 :"))


if ( a1/80*100 > 33 and a2/80*100 > 33 and a3/80*100 > 33 ):
    if (a1+a2+a3)/240*100>40:
        print("Pass")
else:
    print("Fail")