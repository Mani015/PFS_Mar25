
# Python CSV
# A CSV (Comma Separated Values) format is one of the most simple and common ways to store tabular data.
# To represent a CSV file, it must be saved with the .csv file extension.


# Working with CSV files in Python
# While we could use the built-in open() function to work with CSV files in Python,
# there is a dedicated csv module that makes working with CSV files much easier.


import csv

# with open('emp1.csv','w') as file:
#
#     new_file = csv.writer(file)  # writer is a object
#     print(type(new_file))
#     # <class '_csv.writer'>


with open('emp1.csv','w') as file:
    new_file = csv.writer(file)
    new_file.writerow(['eid','eName','eSalary','eDep','eLocation','eDesignation']) # columns

    while True:
        Eid = int(input('Enter your id :'))
        Ename = input('Enter your name : ')
        Esalary = int(input('Enter your salary :'))
        Edep = input('Enter your department :')
        Eloca = input('Enter your location :')
        Edes = input('Enter your designation : ')
        new_file.writerow([Eid,Ename,Esalary,Edep,Eloca,Edes])

        Option = input('Do you want to add one more record  YES | No : ')
        if Option.lower() == 'no':
            break



