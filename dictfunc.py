MyDictionary = {
    'Name': 'Identity',
    'Age': 'How old a person is',
    'Clothes': 'we Wear To cover body',
    'Marks': [1, 2, 5, 5],
    'AnotherD': {"aj": "XAJX"},
    1: 'wow',
    'wow': 1

}

print('\n',MyDictionary.keys(),'\n\n')
print(MyDictionary.values(),'\n\n')
print(MyDictionary.items(),'\n\n')
print(list(MyDictionary.keys()),'\n\n')
print(list(MyDictionary.values()),'\n\n')
print(list(MyDictionary.items()),'\n\n')
print(MyDictionary,'\n\n')

updateDict = {
    "A Name" : "Peter",
    "love":"Yourself First",
    1: 'WOWZA'
}
MyDictionary.update(updateDict)
print(MyDictionary)

print(MyDictionary.get('A Name2'))#wont throw error in wrong
print(MyDictionary['A Name2'])# throws error