# import the sqlite3 module
import sqlite3

# Define connection and cursor
connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# create table
cursor.execute("DROP TABLE IF EXISTS STUDENT")
createTable = '''CREATE TABLE STUDENT(
Student_ID INTEGER PRIMARY KEY AUTOINCREMENT, First_Name VARCHAR(100),
Last_Name VARCHAR(100), Age int,
Department VARCHAR(100)
)'''
cursor.execute(createTable)

# # check the database creation data
# if cursor:
#     print("Database Created Successfully !")
# else:
#     print("Database Creation Failed !")

# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES (1,'Rohit', 'Pathak', 21, 'IT')")
cursor.execute("INSERT INTO STUDENT VALUES (2,'Nitin', 'Biradar', 21, 'IT')")
cursor.execute("INSERT INTO STUDENT VALUES (3,'Virat', 'Kohli', 30, 'CIVIL')")
cursor.execute("INSERT INTO STUDENT VALUES (4,'Rohit', 'Sharma', 32, 'COMP')")

# # printing the cursor data
# if cursor:
#     print("Data Inserted !")
# else:
#     print("Data Insertion Failed !")

# WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT * FROM STUDENT WHERE Department = 'IT'")
cursor.execute("SELECT * from STUDENT WHERE First_name Like'R%'")

# WHERE CLAUSE TO UPDATE DATA
cursor.execute("UPDATE STUDENT SET Department ='E&TC' WHERE Student_ID = 2")
cursor.execute("DELETE from STUDENT WHERE Age = 32")
cursor.execute(
    "INSERT INTO STUDENT VALUES (4,'Ritwik', 'Sharma', 38, 'CIVIL')")
cursor.execute("SELECT * from STUDENT")

# printing the cursor data
print(cursor.fetchall())

# Commit the changes in database and Close the connection
connection.commit()
connection.close()
