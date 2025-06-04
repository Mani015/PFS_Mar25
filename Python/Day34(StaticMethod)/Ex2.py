

# Advantages of a Static Method
# Here, the static method has the following advantages
#
# Consume Less memory: Instance methods are object too, and creating them has a cost. Having a static method avoids that.
# Let’s assume you have ten employee objects and if you create gather_requirement() as a instance method then Python have to create a ten copies of this method (seperate for each object) which will consume more memeory. On the other hand static method has only one copy per class.
#
# To Write Utility functions: Static methods have limited use because they don’t have access to the attributes of an object (instance variables) and class attributes (class variables).