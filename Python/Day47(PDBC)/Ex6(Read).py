import mysql.connector
v1 = mysql.connector.connect(host='localhost',user='root',password='root',database='oreo')
v2 = v1.cursor()

# To see the records from the table using this querry
# sy : 'select * from TableName'

v2.execute('select * from Student')

for var in v2:
    print(var)
# (1, 'Manoj', 'kumar', 12)
# (2, 'lavanya', 'lavanya', 10)
# (3, 'neelaveni', 'neelaveni', 15)
# (4, 'kiran', 'reddy', 17)
