
# Logical Operator : it returns Boolean expression
# There are 3 types of Operands
# and, or, not 



"""PYTHON RESERVED KEYWORDS
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
   'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""

# and : 
print(True and True)  #True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# and statements : 
# When the X is True , then it returns Y value
# When the X is False, then it returns X value

print(4 and 2) # 2
print(5 and 4) # 4

print(10 and 20) # 20

print(0 and 3) # 0

# In python defaultly these are False :  False,0,'',[],(),{}  

# >>> bool('')
# False
# >>> bool(0)
# False
# >>> bool(False)
# False
# >>> bool([])
# False
# >>> bool(())
# False
# >>> bool({})
# False