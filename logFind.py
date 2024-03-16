content=True
i=1
with open('log.txt') as f:

    while content:
        content = f.readline()

        if 'python' in content.lower():
            print(f'Present at {i}')
        i+=1
