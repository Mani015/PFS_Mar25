
# matter = open('info.txt','a')
# matter.write("This is second line")
# matter.write("This is third line")
# print(matter)
# matter.close()






# matter = open('info.txt','a')
# matter.write("This is second line")
# matter.write("\nThis is third line")
# print(matter)
# matter.close()


r1 = open('info.txt','r')
# print(r1.read())
# This is second line
# This is third line
# This is Fourth line
# This is fifth line

# readline()	The readline() method reads a single line from a file at a time.
# Accepts optional size parameter that mentions how many bytes to return from the file.

# print(r1.readline(),end='')
# This is second line

# print(r1.readline())
# This is third line

# readlines()	The readlines() method returns a list of lines from the file.

print(r1.readlines())
# ['This is second line\n', 'This is third line\n', 'This is Fourth line\n', 'This is fifth line\n']

seek, tell,