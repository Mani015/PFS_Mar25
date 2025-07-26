
import mysql.connector
v1 = mysql.connector.connect(host='localhost',user='root',password='root',database='oreo')
v2 = v1.cursor()

# sy : insert into TableName(sno,fname,lanem,age) values (1,'abc','def',12)


# %s:
#  This part indicates that you're providing values to be inserted into the columns.
#  The %s placeholders are used for string formatting and represent where actual values will be inserted.
#
#  The %s placeholders are placeholders for values that you want to insert into the corresponding columns.
#  The number of %s placeholders matches the number of columns specified in the column list.
#  These placeholders are used to prevent SQL injection by properly escaping and formatting the values before they are inserted into the SQL query.
Data = "Insert into Student(sno,fname,lname,age) values(%s, %s, %s,%s)"
# values = [(1,'Manoj','kumar',12)]
values = [(2,'lavanya','lavanya',10),(3,'neelaveni','neelaveni',15),(4,'kiran','reddy',17)]


v2.executemany(Data,values)

v1.commit()
