import mysql.connector as mariadb
con = mariadb.connect(host='localhost',user = 'user1',password = 'abc@123', database='Employee')
        
print("Cnnection established successfully")
cur=con.cursor()
cur.execute("update Employee set salary=salary+10000")

print("no of rows updated",cur.rowcount)
print("updated")
cur.close()
con.commit()
con.close()
