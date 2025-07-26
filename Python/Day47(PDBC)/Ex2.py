
# 1).Install MySQL connector module
# Use the pip command to install MySQL connector Python.
# pip install mysql-connector-python
#
# 2).Import MySQL connector module
# Import using a import mysql.connector statement so you can use this module’s methods to communicate with the MySQL database.
#
# 3).Use the connect() method
# Use the connect() method of the MySQL Connector class with the required arguments to connect MySQL. It would return a MySQLConnection object if the connection established successfully
#
# 4).Use the cursor() method

import  mysql.connector

ob1 = mysql.connector.connect(user='root',host='localhost',password='root')

ob2 = ob1.cursor() #Use the cursor() method of a MySQLConnection object to create a cursor object to perform various SQL operations.

# TO see the how many database in my DBServer
# mysql : show databases;
# python : show databases (this query pass inside excute method)

ob2.execute('show databases')
# print(show)

for i in ob2:
    print(i)
# ('blog',)
# ('clincidb',)
# ('db',)
# ('employee',)
# ('information_schema',)
# ('mango',)
# ('meow',)
# ('mysql',)
# ('patient',)
# ('pencil',)
# ('performance_schema',)
# ('school',)
# ('studb',)
# ('sys',)

