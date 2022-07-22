import mysql.connector as mariadb
con = mariadb.connect(host='localhost',user = 'user1',password = 'abc@123', database='Employee')
        
print("Cnnection established successfully")
cur=con.cursor()
cur.execute("insert into Employee values(1007,'Rita','developer',1001,'2001-09-08','50000',20)")
print("Data Added successful")
cur.close()
con.commit()
con.close()
