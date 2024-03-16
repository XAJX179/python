with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print(f'Present at ')
else:
    print('Not Present. F')
