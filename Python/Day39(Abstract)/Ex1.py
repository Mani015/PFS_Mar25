"""
An abstract class can be considered as a blueprint for other classes.
 It allows you to create a set of methods that must be created within any child classes built from the abstract class.
 A class which contains one or more abstract methods is called an abstract class.
An abstract method is a method that has a declaration but does not have an implementation.
While we are designing large functional units we use an abstract class.
When we want to provide a common interface for different implementations of a component, we use an abstract class.
"""



class Animal(object):

    def Eating(self):
        print('Eating something XYZ')

    def Running(self):
        print('Running some distance from X to Y')

    def Sound(self):
        print('producing sound 50DB')

class Tiger(Animal):

    def Eating(self):
        print('Except grass, Eat everything')

    def Running(self):
        print('Running speed 100km/h')

    def Sound(self):
        print('Producing sound 100DB')


class Cat(Animal):

    def Eating(self):
        print('Cats eats rats + Curd rice + Milk')

    def Running(self):
        print('Running speed 30km/h')

    def Sound(self):
        print('Sounds meow')



class Vehicle(object):

    def Noofwheels(self):
        print('No.of wheels')

    def Speed(self):
        print('Add vehicle speed')

    def Milage(self):
        print('Add vehicle milage')


class Lorry(Vehicle):
    pass

class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

