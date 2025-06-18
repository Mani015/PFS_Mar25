# A class which contains one or more abstract methods is called an abstract class.


# Why use Abstract Base Classes :
# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.
# This capability is especially useful in situations where a third-party is going to provide implementations,
# such as with plugins, but can also help you when working in a large team or with a large code-base
# where keeping all classes in your mind is difficult or not possible.
#
# How Abstract Base classes work :
# By default, Python does not provide abstract classes.
#  Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
#  ABC works by decorating methods of the base class as abstract and then registering concrete classes as
# implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.

from abc import ABC,abstractmethod


class Vehicle(ABC):
    #A method becomes abstract when decorated with the keyword @abstractmethod.
    @abstractmethod
    def Noofwheels(self):
        ...

    @abstractmethod
    def Speed(self):
        pass

    @abstractmethod
    def Milage(self):
        pass



# ob1  : Vehicle =  Vehicle()
# ob1.Noofwheels()
# TypeError: Can't instantiate abstract class Vehicle with abstract methods Milage, Noofwheels, Speed


class Car(Vehicle):

    def Noofwheels(self):
        print('Having a car Four wheels')

    def Milage(self):
        print('Car give a milage 20km/li')

    def Speed(self):
        print('Speed is 130km/h')


Benz  :Car = Car()
Benz.Noofwheels()
Benz.Speed()
Benz.Milage()

# Having a car Four wheels
# Speed is 130km/h
# Car give a milage 20km/li

