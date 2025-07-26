
import mysql.connector
v1 = mysql.connector.connect(host='localhost',user='root',password='root',database='oreo')
v2 = v1.cursor()

# sy : update tablename set col = value where col = value

v2.execute('update student set lname = "pythondeveloper" where sno = 2')

v1.commit()
