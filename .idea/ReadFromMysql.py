# This is an example to demonstrate SQL connect to MySQL database in AWS.
# I have leveraged MySql connector package in this example.

import mysql.connector
from mysql.connector import Error

# Open JDBC connection to RDS (Relational Data Store).
try:
    mySQLconnection = mysql.connector.connect(host='mysqlinstance.cedrsrjifutx.us-east-2.rds.amazonaws.com',
                                              database='sys',
                                              user='mysqluser',
                                              password='mysqlpassword')

    # Execute select statement
    sql_select_Query = "select * from sys.sys_config"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)

    # Open the cursor, fetch the resultset and print
    records = cursor.fetchall()
    print("Total number of rows - ", cursor.rowcount)
    print ("Printing Database records")
    for row in records:
        print("Variable = ", row[0], )
        print("Value = ", row[1])
        print("Set Time  = ", row[2])
        print("Set By  = ", row[3], "\n")
    cursor.close()

# Handle exceptions if any
except Error as e :
    print ("Error while connecting to AmazonAWS", e)

# Graceful exit in the final block
finally:
    #closing database connection.
    if(mySQLconnection.is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")