
import mysql.connector
v1 = mysql.connector.connect(host='localhost',user='root',password='root')
v2 = v1.cursor()

# mysql sy  : create database Database_name;
create = "create database oreo"

# 5).Use the execute() method
# The execute() methods run the SQL query and return the result.

v2.execute(create)
print(v2)
