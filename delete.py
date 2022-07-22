import mysql.connector as mariadb
con = mariadb.connect(host='localhost',user = 'user1',password = 'abc@123', database='Employee')
        
print("Cnnection established successfully")
cur=con.cursor()
cur.execute("delete from Department where dname='Sales'")
print("no of rows deleted",cur.rowcount)
print("done`")
cur.close()
con.commit()
con.close()
