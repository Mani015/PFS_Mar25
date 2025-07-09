# read a file with keyword
"""
with open('info1','r') as file:
    new = file
    print(new.readlines())

print('is it close file ? :', file.closed)"""
# ['Mangos are very sweetbanana is a yellow color fruit\n', '2025 summer is too hot\n', '2025 summer is too hot\n', '2025 winter is so cold\n', '2025 rainy season is called a  trouble season']
# is it close file ? : True


# Read the file First N lines
"""
with open('info1','r') as file:
    new_file = file
    N = int(input('Enter N line : '))
    for i in range(N):
        print(new_file.readline(),end='')

Enter N line : 4
Mangos are very sweetbanana is a yellow color fruit
2025 summer is too hot
2025 summer is too hot
2025 winter is so cold"""

# Read a file First line and last line

"""with open('info1','r') as file:
    # reading the first line
    First_line = file
    print(First_line.readline())
    # reading the last_line
    for last_line in file:
        pass
    print(last_line)
Mangos are very sweetbanana is a yellow color fruit

2025 rainy season is called a  trouble season"""

# we can use realine() method to read the entire file using the while loop . we need to check wheather the pointer has reached the end of the file and then loop through the file line by line
"""with open('info1', 'r') as fp:
    # Read the first line
    line = fp.readline()
    # Iterate the file till it reached the EOF
    while line != '':
        print(line, end='')
        line = fp.readline()


Mangos are very sweetbanana is a yellow color fruit
2025 summer is too hot
2025 summer is too hot
2025 winter is so cold
2025 rainy season is called a  trouble season"""
