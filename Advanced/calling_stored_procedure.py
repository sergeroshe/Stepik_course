import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql@_-',
    port='3306',
    database='classicmodels'
)
mycursor = mydb.cursor()
users = mycursor.fetchall()

for user in users:
    print(user)
    print('Username: ' + user[1])
    print('Password: ' + user[2])
