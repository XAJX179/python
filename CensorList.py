_censored_words=["fuck","shit","idiot","dick"]

with open('sample.txt')as f:
    data_of_file =  f.read()

for i in _censored_words:
    data_of_file = data_of_file.replace(i,'$#%^%')

with  open('sample.txt','w')as f:
    f.write(data_of_file)