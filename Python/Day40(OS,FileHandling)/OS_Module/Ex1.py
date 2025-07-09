
import os

# getcwd : get current working directory
# print(os.getcwd())
# C:\Users\Test\PycharmProjects\pythonProject\PFS_Mar25\Python\Day40(OS,FileHandling)

# We need to change directory
# chdir(path) : change directory

os.chdir("C:\\Users\Test\Desktop\Python\Python_Definations")
# print(os.getcwd())
# C:\Users\Test\Desktop\Python\Python_Definations


# what are the files in particular directory
# listdir()

Path_dir = "C:\\Users\Test\Desktop\Python\Python_Definations"

All_files = os.listdir(Path_dir)
# print(All_files)

for file in All_files:
    print(f'Name : {file}')

# Name : Array typecodes.png
# Name : Computer-Transilator.txt
# Name : DataTypes(list,Tuple,Set).txt
# Name : Decorator.png
# Name : Decorator.txt
# Name : Encapsulation
# Name : Encapsulation.txt
# Name : encapsulation_python_class.jpg
# Name : Ephesians-Study-Questions.pdf
# Name : Exception_Handling.txt
# Name : File_Handling.txt
# Name : For loops.txt
# Name : Functions.txt
# Name : Galatians_Ephesians_Philippians_Colossians_Philemon.pdf
# Name : Generator.txt
# Name : Handling CSV.txt
# Name : Instance vs class vs static methods.jpeg
# Name : Instance_Class_Static methods.txt
# Name : Keywords in Python.txt
# Name : LEGB-Rules.txt
# Name : Libraries
# Name : List.txt
# Name : Map,Filter,Reduce.txt
# Name : Matplotlib.txt
# Name : Modules.txt
# Name : Music Project.txt
# Name : Mutli_Threading.txt
# Name : MYSQL
# Name : Mysql - updateallrecords at a time.txt
# Name : Numpy - Shortcut.lnk
# Name : Numpy.txt
# Name : object_properties.webp
# Name : OOPS_2_Inheritance.txt
# Name : OOPS_Abstraction.txt
# Name : OOPS_Class&Object.txt
# Name : OOPS_POLY.txt
# Name : os-module.txt
# Name : osmodule.txt
# Name : Pandas.txt
# Name : PDBC.png
# Name : PDBC.txt
# Name : product.jpg
# Name : python notes sm.txt
# Name : python-language.png
# Name : PythonBasicIntro.txt
# Name : Python_Ascii value.png
# Name : python_data_hiding.jpg
# Name : Recursion
# Name : RegularEx.txt
# Name : Scope_of_varaibles.txt
# Name : student.png
# Name : Time_Module.txt
# Name : TypeCasting.txt
# Name : TypesofArguments.txt