HindiDict = {
    "Dahi":'Curd',
    "Angur":'Grapes',
    'Dabba':'Box'
}
print("Options are :",HindiDict.keys())
a = input('Enter the Hindi word : ')
print("Meaning of your word is :",HindiDict.get(a))#avoids error