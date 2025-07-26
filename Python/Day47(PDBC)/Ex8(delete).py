

import mysql.connector
v1 = mysql.connector.connect(host='localhost',user='root',password='root',database='oreo')
v2 = v1.cursor()

# delete from Tablename where condition

v2.execute('delete from student where sno = 1')

v1.commit()
