
# Python is an object-oriented programming language.
# This means that almost all the code is implemented using a special construct called classes.
# A class is a code template for creating objects.
#
# What is a Class and Objects in Python?
#
# [Class: The class is a user-defined data structure that binds the data members and methods into a single unit.
# Class is a blueprint or code template for object creation. Using a class, you can create as many objects as you want.]
#
# Object: An object is an instance of a class. It is a collection of attributes (variables) and methods.
#  We use the object of a class to perform actions.
#
#
# Objects have two characteristics: They have states and behaviors (object has attributes and methods attached to it) Attributes represent its state,
# and methods represent its behavior. Using its methods, we can modify its state.
#
# In short, Every object has the following property.
#
# Identity: Every object must be uniquely identified.
# State: An object has an attribute that represents a state of an object, and it also reflects the property of an object.
# Behavior: An object has methods that represent its behavior.
#
# A real-life example of class and objects.
#
# Class: Person
#
# State: Name, Gender, Profession
#
# Behavior: Working, Study
#
# Using the above class, we can create multiple objects that depict different states and behavior.
#
# Object 1: Jessa
#
# State:
# Name: Jessa
# Gender: Female
# Profession: Software Engineer
#
# Behavior:
# Working: She is working as a software developer at ABC Company
# Study: She studies 2 hours a day
#
# Object 2:
#
# State:
# Name: John
# Gender: Male
# Profession: Doctor
#
# Behavior:
# Working: He is working as a doctor
# Study: He studies 5 hours a day


# syntax:
# class ClassName(object):
#
#     statement.....1
#     statement.....2
#     statement.....N


# How to create empty class
class Student:pass


# creating a class with name
class Person(object):
    Name : str = "Suresh"  # attribute1
    Age : int = 20 # attribute1
    Location : str = "India"  # attribute1
    Profession : str = "Softwate developer"  # attribute1


# calling attributes with classname
# sy : className.attributeName
print(f'Name : {Person.Name}')
print(f'Age : {Person.Age}')
print(f'location : {Person.Location}')
print(f'Profes : {Person.Profession}')


# Name : Suresh
# Age : 20
# location : India
# Profes : Softwate developer

