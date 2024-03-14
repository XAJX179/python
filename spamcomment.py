string = input("Enter Comment: \n")


if("make money"in string):
    spam = True
elif "buy this" in string:
    spam = True
elif "offer free"in string:
    spam = True
else:
    spam = False

if (spam):
    print("Spam")
else:
    print(string)