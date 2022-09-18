import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ankkalinna',
         user='root',
         password='1999',
         autocommit=True
         )