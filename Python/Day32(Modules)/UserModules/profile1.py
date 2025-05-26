

print('Main Script being run')

# Just want to know name of this module
print('Current Name : ', __name__)
# Current Name :  __main__

def Current():

    print('My name is Main FIle')


if __name__ == '__main__':
    print('In this main file nothing will be executing')

else:
    Current()

# Main Script being run
# Current Name :  __main__
# In this main file nothing will be executing



# The if __name__ == '__main__': statement in Python serves as a conditional check to determine how a script is being executed.
# When a Python file is run directly, the special variable __name__ is set to the string '__main__'.
# However, if the file is imported as a module into another script, __name__ is set to the name of the module.