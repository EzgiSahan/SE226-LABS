import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ata35zhm75"
)

cursorObject = database.cursor()
cursorObject.execute("DROP DATABASE IF EXISTS Marvel")
create = "CREATE DATABASE Marvel"
cursorObject.execute(create)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ata35zhm75",
    database='Marvel'
)

if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

try:
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password='ata35zhm75',
                                         database='Marvel')
    cursorObject = connection.cursor()
    cursorObject.execute("DROP TABLE IF EXIST Movies")
    mysql_Create_Table_Query = """CREATE TABLE Movies (
                                  ID INT,
                                  MOVIE VARCHAR(250),
                                  DATE VARCHAR(250),
                                  MCU_PHASE VARCHAR(250)"""
    result = cursorObject.execute(mysql_Create_Table_Query)
    print("Movies created successfully ")
    cursorObject.execute("SHOW TABLES")

    for table_name in cursorObject:
        print(table_name)

except mysql.connector.Error as error:
    print("Failed to create table in MySql: {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySql connection is closed")

path = open('/Users/ezgi/Desktop/Marvel.txt')

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password='ata35zhm75',
        database='Marvel')
    cursorObject = connection.cursor()

    while path:
        text = path.readline()
        if text == " ":
            break
        splitLine = text.split()
        Insert = """INSERT INTO Movies(ID, MOVIE, DATE, MCU_PHASE)
        VALUES(%s, %s, %s, %s)"""
        record = (splitLine[0], splitLine[1], splitLine[2], splitLine[3])
        cursorObject.execute(Insert, record)
        connection.commit()
    print("Records are added into Movies table.")

except mysql.connector.Error as error:
    print("Failed to insert record into Movies table {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed.")

try:
    connection = mysql.connector.connect(
        host="localhost",
        database='Marvel',
        user="root",
        password='ata35zhm75')
    sql_select = "SELECT * FROM Movies"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_select)
    records = cursorObject.fetchall()
    for row in records:
        print(row)

except mysql.connector.Error as error:
    print("Error reading data from MySQL table", error)
finally:
    if connection.is_connected():
        connection.close()
        cursorObject.close()
        print("MySQL connection is closed.")

try:
    connection = mysql.connector.connect(
        host="localhost",
        database='Marvel',
        user="root",
        password='ata35zhm75')
    sql_remove = "DELETE FROM Movies WHERE Movies = 'TheIncredibleHulk'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_remove)
    connection.commit()
    print("Record deleted successfully from Movies table.")
except mysql.connector.Error as error:
    print("Error deleting data from MySQL table", error)
finally:
    if connection.is_connected():
        connection.close()
        cursorObject.close()
        print("MySQL connection is closed.")

try:
    connection = mysql.connector.connect(
        host="localhost",
        database='Marvel',
        user="root",
        password='ata35zhm75')
    sql_list = "SELECT * FROM Movies WHERE MCU_PHASE = 'Phase2'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_list)
    records1 = cursorObject.fetchall()
    for row1 in records1:
        print(row1)
except mysql.connector.Error as error:
    print("Failed to insert record into Movies table {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed.")
try:
    connection = mysql.connector.connect(
        host="localhost",
        database='Marvel',
        user="root",
        password='ata35zhm75')

    sql_update = "UPDATE Movies SET DATE = 'November 3, 2017' WHERE MOVIE = 'Thor:Ragnarok'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_update)
    connection.commit()

except mysql.connector.Error as error:
    print("Error updating data in MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed.")
