
import csv

with open('emp1.csv','w',newline='') as file:
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

