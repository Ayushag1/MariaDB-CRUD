import mysql.connector as mariadb
con = mariadb.connect(host='localhost',user = 'user1',password = 'abc@123', database='employee')
        
print("Cnnection established successfully")
con.close()


