
# What is an abstract class in Python?
# What is an interface in Python?
# Difference between abstract class and interface in Python
#
# What is an Abstract class in Python?
# A blueprint for other classes might be thought of as an abstract class. You may use it to define a collection of methods th
#
#
# 1.what is the advantage of declaring abstract methods in Parent class ?
# a).By declaring abstract methods in parent class we can providing guidelines to the child classes,
#  such that which methods compulsory they should implement.
#
# 2. Is a class can contain both abstract and non-abstract methods ?
# a).yes
# Note : if a class contains both abstract and non-abstract methods then child class is responsible to provide implementation only for abstract methods.
#
# The Most Important Conclusion :
# 1.If a class contains at least one abstract mehtods and if we are extending ABC class then instantiation is not possible.
# " For Abstract class with abstract methods, instantiation is not possible ".
#
#
#
# What is an Interface in Python?
# 1.An abstract class can contains both abstract and non-abstract methods.
# 2.If an abstract class contains only abstract methods, such type of abstract class is nothing but interface.
# 3.100% pure abstract class is nothing but interface.
# Interface simply acts as a Service Requirement Specifications(SRS).
#
# The interface in object-oriented languages like Python is a set of method signatures that the implementing class is expected to provide.
# Writing ordered code and achieving abstraction are both possible through interface implementation.
#
# Example:
#
# Python “object interfaces” are implemented in the module zope.interface.  It is maintained by the Zope Toolkit project. Two objects, “Interface” and “Attribute,” are directly exported by the package. Several helper methods are also exported by it. Compared to Python’s built-in abc module, it strives to give stronger semantics and better error messages.
#
# Declaring interface: In Python, an interface is defined using Python class statements and is a subclass of interface.Interface which is the parent interface for all interfaces.
#
#
# Implementing interface: The interface acts as a blueprint for designing classes,
# so interfaces are implemented using the implementer decorator on the class.
# If a class implements an interface,then the instances of the class provide the interface. Objects can provide interfaces directly,
# in addition to what their classes implement.
#
# Interface acts as a requirement specification,proto type to implement for a particular software
#
#
#
# Difference between abstract class and interface in Python?
#
# Abstract Class                                                                                                   Interface
# 1.	An abstract features developer’s class can consist of abstract as well as concrete methods  |	All methods of an interface are abstract
# 2.	It is used when there are some common feature shared by all objects	                    |   It is used when all the feature need to be implemented differently for different objects
# 3.	Its developer responsibility to create a child class for the features of an abstract class  |	Any 3rd person will responsible for creating a child class
# 4.	It is comparatively fast	                                                            |    It is comparatively slow
#
#
#
#
# Interface vs Abstract class Vs Concentrate class :
# 1.If we don't know anything about implementation, then just we have requirement specification then we should go for interface.(SRS, Service Requirement Specification)
#
# 2.If we are talking about implementation but not completely then we should go for abstract class (partially implementd class)
#
# 3.We are talk about implementation completely and ready to provide service then we should go for concrete class(Fully completed class).