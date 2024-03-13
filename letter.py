letter='''
Hello |NAME|,

You are rejected.
DONT CARE GO CRY

|DATE|
'''
name = str(input("Enter Name :"))
da = (input("Enter Date:"))

letter = letter.replace('|NAME|',name)
letter = letter.replace('|DATE|',da)

print(letter)