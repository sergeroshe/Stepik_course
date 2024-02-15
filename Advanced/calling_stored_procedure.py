import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql@_-',
    port='3306',
    database='classicmodels'
)
cursorObject = mydb.cursor()

query = "CALL classicmodels.show_customers()"
cursorObject.execute(query)

query_result = cursorObject.fetchall()

for el in query_result:
    print(el)

# disconnecting from server
mydb.close()
# show_customers_proc = 'CALL classicmodels.show_customers()'
#
# # table created
# cursorObject.execute(show_customers_proc)
#
# # disconnecting from server
# mydb.close()



