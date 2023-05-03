"""SQLITE DATABASE REFERENCE/TUTORIAL FILE, FORMAT AND PASTE FINDINGS HERE"""

#Reference: https://www.youtube.com/watch?v=byHcYRpMgI4&ab_channel=freeCodeCamp.org
"""
SQLite in Python has 5 Datatypes:
NULL
INTEGER
REAL - decimal
TEXT
BLOB - image,mp3 file
(?) - placeholder for value
"""

import sqlite3

"""Database"""
#connection = sqlite3.connect(':memory:') For temporary storage and testing uncomment this.
connection = sqlite3.connect('landlord.db')

#Cursor tells the database what to do
curs = connection.cursor() #Creates cursor

"""Create Table"""
#Every time John receives a payment, he records the payment in the appropriate column (month) and row (apartment_number)
curs.execute("""CREATE TABLE rental_income (
        month INTEGER,
        apartment_number INTEGER,
        payment REAL
    )""")

"""Drop Table"""
#Just for knowledge, no need to actually use it.
#curs.execute("DROP TABLE rental_income")

"""Insert Data"""
curs.execute("INSERT INTO rental_income (month, apartment_number, payment) VALUES (?,?,?)", )

"""Query Data"""
curs.execute("SELECT rowid, * FROM rental_income LIMIT 3") #limits everything selected to 3 results.
#SQL automatically creates primary key rowid for each record added.
#curs.execute("SELECT * FROM rental_income WHERE month = 1 OR month = 3")
#curs.execute("SELECT * FROM expense_record WHERE payee LIKE '%test' AND rowid = 4")
#Example of filtering data
curs.execute("SELECT rowid, * FROM rental_income ORDER BY month") #Ascdending by default
curs.execute("SELECT rowid, * FROM rental_income ORDER BY month DESC") #Descending order

"""Update Records"""
#DO NOT USE WITHOUT USING THE PK (ROWID) OR YOU WILL CORRUPT THE DATA
curs.execute("""UPDATE rental_income SET month = 1
                WHERE rowid = 2""")

"""Delete Records"""
#DO NOT USE WITHOUT USING THE PK (ROWID) OR YOU WILL CORRUPT THE DATA
curs.execute("DELETE from rental_income WHERE rowid = 3")

"""Retrieve Data"""
#curs.fetchone() #Fethches first item of a specified table
#curs.fetchmany() #Fetches first given number of items of specified table
dbRIList = curs.fetchall() #Fetches everything in the rental_income table and assigns it to var
''' Data in the data base is organized by a list of tuples. 
    For example in rental_income the expected tuple would be
    (month, apartment_number, payment) To access each specific
    part of each record, specify by the index. For example to 
    access month at index 0 of the first record of the database
    use curs.fetchone()[0]
    or
    for dbRITuple in dbRIList:
    print(dbRITuple[0], dbRITuple[1], dbRITuple[2]) 
    #Items in tuple in the list
    '''

"""Commiting Commands to Database"""
#Executes the above commands specified in the file.
connection.commit()

"""Close Connection"""
connection.close()