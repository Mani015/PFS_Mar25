

import os

current_path = "C:\\Users\\Test\\Desktop\\Macbook\\"

count = 1
for file in os.listdir(current_path):
    source = current_path + file
    # print(source)

    destination = current_path + 'demo' + str(count) + '.py'

    os.rename(source, destination)

    count = count + 1


print('All files are renamed')

file = os.listdir(current_path)
print(file)


#
#
l1 = ['file1','file2','file3','ex1.py','ex2.py','ex3.py']

for file in l1:
    if file in ['file1','file2','file3']:

        print(f'Yes {file} is exist')
    else:
        print(f'sorry {file} does not exists')
