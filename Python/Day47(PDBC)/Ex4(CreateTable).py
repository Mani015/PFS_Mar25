
import mysql.connector
v1 = mysql.connector.connect(host='localhost',user='root',password='root',database='oreo')
v2 = v1.cursor()

# Create table
# sy : create table Table_Name(col1 dtype,col2 dtype, col3 dtype.............)

Table = "Create table student(sno int, Fname varchar(30),Lname varchar(30), age int)"

# v2.execute(Table)
# print(v2)
# CMySQLCursor: Create table student(sno int, Fname varc..


# TO see what are the column names;
# sy : desc table_name
v2.execute('desc student')
for k in v2:
    print(k)

# ('sno', 'int', 'YES', '', None, '')
# ('Fname', 'varchar(30)', 'YES', '', None, '')
# ('Lname', 'varchar(30)', 'YES', '', None, '')
# ('age', 'int', 'YES', '', None, '')
