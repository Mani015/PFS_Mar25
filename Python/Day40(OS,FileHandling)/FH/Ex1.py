
# What is File?
# Files are named location on disk to store information
# They are used to data permanently.
# We  can retrived data whenever required
#
# Types of File
# Text File: Text file usually we use to store character data. For example, test.txt
# Binary File: The binary files are used to store binary data such as images, video files, audio files, etc.
#
# Create File in Python: You'll learn to create a file in the current directory or a specified directory.
#  Also, create a file with a date and time as its name. Finally, create a file with permissions.
# Create A Empty Text File
# We don’t have to import any module to create a new file. We can create a file using the built-in function open().

# sy : open(file_name,mode)
file1 = open('info.txt','x')
print(file1)
# <_io.TextIOWrapper name='info.txt' mode='x' encoding='cp1252'>


# FileExistsError: [Errno 17] File exists: 'info.txt'

# Below is the list of access modes for creating an a file.
#
# File Mode	Meaning
# w		Create a new file for writing. If a file already exists, it truncates the file first.
# 		Use to create and write content into a new file.
# x		Open a file only for exclusive creation. If the file already exists, this operation fails.
# a		Open a file in the append mode and add new content at the end of the file.
# b		Create a binary file
# t		Create and open a file in a text mode
# r		Read the data in this file


