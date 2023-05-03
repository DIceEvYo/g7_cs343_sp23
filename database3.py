import sqlite3

"Perform Queries"

def performQuery(query):
    connection = sqlite3.connect('landlord.db')  # Connect to DB
    curs = connection.cursor()  # Cursor tells the database what to do
    curs.execute(query)
    result = curs.fetchall()
    curs.close()
    return result

def recordPerformQuery(query, fileName):
    QueryRecordFile = open(fileName, "w")
    connection = sqlite3.connect('landlord.db')  # Connect to DB
    curs = connection.cursor()  # Cursor tells the database what to do
    queryResults = curs.execute(query)
    for queryList in queryResults:
        index = 0
        for data in queryList:
            if (index < len(queryList)-1):
                QueryRecordFile.write(str(data) + ", ")
                index += 1
            else:
                QueryRecordFile.write(str(data)+ "\n")
    QueryRecordFile.close()

def displayPerformQuery(query):
    connection = sqlite3.connect('landlord.db')  # Connect to DB
    curs = connection.cursor()  # Cursor tells the database what to do
    queryResults = curs.execute(query)
    for queryList in queryResults:
        index = 0
        temp = ""
        for data in queryList:
            if (index < len(queryList)-1):
                temp = temp + (str(data) + ", ")
                index += 1
            else:
                temp = temp + (str(data))
                print(temp)

""" 
    RENTAL INCOME
    "The Rental Income Record records incoming rent payments. It contains 12 columns, one for
    each month; and one row for each apartment number. Each time John receives a rental payment
    from a tenant, he records it in the appropriate row and columns of the Rental Income Record."
    - Request for Proposal.docx
    month: Type TEXT (JAN, FEB, etc.)
    payment: Type REAL (decimal)
    tenant_id: Type INT
"""

def createTableRentalIncome():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor()  #Cursor tells the database what to do
    curs.execute("""CREATE TABLE rental_income (
            month TEXT,
            payment REAL,
            tenant_id INTEGER
        )""")
    connection.commit()
    connection.close()

def dropTableRentalIncome():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor()  #Cursor tells the database what to do
    curs.execute("DROP TABLE rental_income")
    connection.commit()
    connection.close()

def displayRentalIncome():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("SELECT rowid, * FROM rental_income")
    dbRIList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbRITuple in dbRIList:
        print(str(dbRITuple[0]) + ", " + str(dbRITuple[1])  + ", " + str(dbRITuple[2])+ ", " + str(dbRITuple[3]))
        #Items in tuple in the list
    connection.commit()
    connection.close()

def displayQueryRentalIncome(query):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute(query)
    dbRIList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbRITuple in dbRIList:
        print(str(dbRITuple[0]) + ", " + str(dbRITuple[1])  + ", " + str(dbRITuple[2]) + ", " + str(dbRITuple[3]))
        #Items in tuple in the list
    connection.commit()
    connection.close()

def writeRentalIncome():
    #Overwrites any prev file data with new data of given table.
    RentalIncomeFile = open("rental_income.txt", "w")
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("SELECT rowid, * FROM rental_income")
    dbRIList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbRITuple in dbRIList:
        RentalIncomeFile.write(str(dbRITuple[0]) + "," + str(dbRITuple[1]) + "," + str(dbRITuple[2])  + "," + str(dbRITuple[3])+ "\n")
        #Items in tuple in the list
    connection.commit()
    connection.close()
    RentalIncomeFile.close()

def writeQueryRentalIncome(query):
    #Overwrites any prev file data with new data of given table.
    RentalIncomeFile = open("rental_income_query.txt", "w")
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute(query)
    dbRIList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbRITuple in dbRIList:
        RentalIncomeFile.write(str(dbRITuple[0]) + "," + str(dbRITuple[1]) + "," + str(dbRITuple[2])  + "," + str(dbRITuple[3])+ "\n")
        #Items in tuple in the list
    connection.commit()
    connection.close()
    RentalIncomeFile.close()

def readRentalIncomeFile():
    #Reads information from rental_income.txt
    RentalIncomeFile = open("rental_income.txt", "r")
    records = []
    index = 0
    for RentalIncomeRecord in RentalIncomeFile:
      records.append([])
      for data in RentalIncomeRecord.split(","):
        records[index].append(data)
      addListRecordRentalIncome(records[index][1:])
      index += 1
    RentalIncomeFile.close()

def addRecordRentalIncome(month, payment, tenant_id):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("INSERT INTO rental_income (month, payment, tenant_id) VALUES (?,?,?)", (month, payment, tenant_id))
    connection.commit()
    connection.close()

def addListRecordRentalIncome(list):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("INSERT INTO rental_income (month, payment, tenant_id) VALUES (?,?,?)", (list))
    connection.commit()
    connection.close()

def delRecordRentalIncome(id):
    #When using this function pass the parameter as a string
    #Ex: database3.delRecordRentalIncome('3')
    connection = sqlite3.connect('landlord.db')  # Connect to DB
    curs = connection.cursor()  # Cursor tells the database what to do
    curs.execute("DELETE from rental_income WHERE rowid = (?)", id)
    connection.commit()
    connection.close()

""" 
    EXPENSE RECORD
    "The Expense Record records outgoing payments. It has columns for date, the payee (the
    company or person to whom John writes the check), and the amount being paid. In addition ,
    there's a column where John can specify the budget category to which the payment should be
    charged. Budget categories include Mortgage, Repairs, Utilities, Taxes, Insurance, and so on."
    - Request for Proposal.docx
    date: Type TEXT, Format as 2023-03-17
    payee : TYPE TEXT
    amount_paid: Type REAL (decimal)
    budget_cat: Type TEXT
"""

def createTableExpenseRecord():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor()  #Cursor tells the database what to do
    curs.execute("""CREATE TABLE expense_record (
            date TEXT,
            payee TEXT,
            amount_paid REAL,
            budget_cat TEXT
        )""")
    connection.commit()
    connection.close()

def dropTableExpenseRecord():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor()  #Cursor tells the database what to do
    curs.execute("DROP TABLE expense_record")
    connection.commit()
    connection.close()

def displayExpenseRecord():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("SELECT rowid, * FROM expense_record")
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        print(str(dbERTuple[0]) + ", " + str(dbERTuple[1]) + ", " + str(dbERTuple[2]) + ", " + str(dbERTuple[3])+ ", " + str(dbERTuple[4]))
        #Items in tuple in the list
    connection.commit()
    connection.close()

def displayQueryExpenseRecord(query):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute(query)
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        print(str(dbERTuple[0]) + ", " + str(dbERTuple[1]) + ", " + str(dbERTuple[2]) + ", " + str(dbERTuple[3])+ ", " + str(dbERTuple[4]))
        #Items in tuple in the list
    connection.commit()
    connection.close()

def writeExpenseRecord():
    #Overwrites any prev file data with new data of given table.
    expenseRecordFile = open("expense_record.txt", "w")
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("SELECT rowid, * FROM expense_record")
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        expenseRecordFile.write(str(dbERTuple[0]) + "," + str(dbERTuple[1]) + "," + str(dbERTuple[2]) + "," + str(dbERTuple[3])  + "," + str(dbERTuple[4]) + "\n")
        #Items in tuple in the list
    connection.commit()
    connection.close()
    expenseRecordFile.close()

def writeQueryExpenseRecord(query):
    #Overwrites any prev file data with new data of given table.
    expenseRecordFile = open("expense_record_query.txt", "w")
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute(query)
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        expenseRecordFile.write(str(dbERTuple[0]) + "," + str(dbERTuple[1]) + "," + str(dbERTuple[2]) + "," + str(dbERTuple[3]) + "," + str(dbERTuple[4]) + "\n")
        #Items in tuple in the list
    connection.commit()
    connection.close()
    expenseRecordFile.close()

def readExpenseRecordFile():
    #Reads information from rental_income.txt
    ExpenseRecordFile = open("expense_record.txt", "r")
    records = []
    index = 0
    for ExpenseRecordRecord in ExpenseRecordFile:
      records.append([])
      for data in ExpenseRecordRecord.split(","):
        if(data.__contains__("\n")):data = data.replace("\n","")
        records[index].append(data)
      addListRecordExpenseRecord(records[index][1:])
      index += 1
    ExpenseRecordFile.close()

def addRecordExpenseRecord(date,payee,amount_paid,budget_cat):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("INSERT INTO expense_record (date,payee,amount_paid,budget_cat) VALUES (?,?,?,?)", (date,payee,amount_paid,budget_cat))
    connection.commit()
    connection.close()

def addListRecordExpenseRecord(list):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("INSERT INTO expense_record (date,payee,amount_paid,budget_cat) VALUES (?,?,?,?)", (list))
    connection.commit()
    connection.close()

def delRecordExpenseRecord(id):
    #When using this function pass the parameter as a string
    #Ex: database3.delRecordRentalIncome('3')
    connection = sqlite3.connect('landlord.db')  # Connect to DB
    curs = connection.cursor()  # Cursor tells the database what to do
    curs.execute("DELETE from expense_record WHERE rowid = (?)", id)
    connection.commit()
    connection.close()

"""
    TENANT LIST
    "The Tenant List shows apartment numbers in one column and the corresponding tenant's names
    in the adjacent columns."
    - Request for Proposal.docx
    first_name: Type TEXT
    last_name: Type TEXT
    apartment_number: Type INT
    phone_number: Type TEXT
    email: Type TEXT
"""

def createTableTenantList():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor()  #Cursor tells the database what to do
    curs.execute("""CREATE TABLE tenant_list (
            first_name TEXT,
            last_name TEXT,
            apartment_number INT,
            phone_number TEXT,
            email TEXT
        )""")
    connection.commit()
    connection.close()

def dropTableTenantList():
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor()  #Cursor tells the database what to do
    curs.execute("DROP TABLE tenant_list")
    connection.commit()
    connection.close()

def displayTenantList(): #TODO
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("SELECT rowid, * FROM tenant_list")
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        print(str(dbERTuple[0]) + ", " + str(dbERTuple[1]) + ", " + str(dbERTuple[2]) + ", " + str(dbERTuple[3])+ ", " + str(dbERTuple[4]) + ", " + str(dbERTuple[5]))
        #Items in tuple in the list
    connection.commit()
    connection.close()

def displayQueryTenantList(query):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute(query)
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        print(str(dbERTuple[0]) + ", " + str(dbERTuple[1]) + ", " + str(dbERTuple[2]) + ", " + str(dbERTuple[3])+ ", " + str(dbERTuple[4]) + ", " + str(dbERTuple[5]))
        #Items in tuple in the list
    connection.commit()
    connection.close()

def writeTenantList():
    #Overwrites any prev file data with new data of given table.
    expenseRecordFile = open("tenant_list.txt", "w")
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("SELECT rowid, * FROM tenant_list")
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        expenseRecordFile.write(str(dbERTuple[0]) + "," + str(dbERTuple[1]) + "," + str(dbERTuple[2]) + "," + str(dbERTuple[3])  + "," + str(dbERTuple[4]) + "," + str(dbERTuple[5]) + "\n")
        #Items in tuple in the list
    connection.commit()
    connection.close()
    expenseRecordFile.close()

def writeQueryTenantList(query):
    #Overwrites any prev file data with new data of given table.
    expenseRecordFile = open("tenant_list_query.txt", "w")
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute(query)
    dbERList = curs.fetchall()  #Fetches everything in above query and assigns it to var
    for dbERTuple in dbERList:
        expenseRecordFile.write(str(dbERTuple[0]) + "," + str(dbERTuple[1]) + "," + str(dbERTuple[2]) + "," + str(dbERTuple[3]) + "," + str(dbERTuple[4]) + "," + str(dbERTuple[5]) + "\n")
        #Items in tuple in the list
    connection.commit()
    connection.close()
    expenseRecordFile.close()

def readTenantListFile():
    #Reads information from rental_income.txt
    TenantListFile = open("tenant_list.txt", "r")
    records = []
    index = 0
    for TenantListRecord in TenantListFile:
      records.append([])
      for data in TenantListRecord.split(","):
        if(data.__contains__("\n")):data = data.replace("\n","")
        records[index].append(data)
      addListRecordTenantList(records[index][1:])
      index += 1
    TenantListFile.close()

def addRecordTenantList(first_name,last_name,apartment_number,phone_number, email):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("INSERT INTO tenant_list (first_name,last_name,apartment_number,phone_number, email) VALUES (?,?,?,?,?)", (first_name,last_name,apartment_number,phone_number, email))
    connection.commit()
    connection.close()

def addListRecordTenantList(list):
    connection = sqlite3.connect('landlord.db') #Connect to DB
    curs = connection.cursor() #Cursor tells the database what to do
    curs.execute("INSERT INTO tenant_list (first_name,last_name,apartment_number,phone_number, email) VALUES (?,?,?,?,?)", (list))
    connection.commit()
    connection.close()

def delRecordTenantList(id):
    #When using this function pass the parameter as a string
    #Ex: database3.delRecordRentalIncome('3')
    connection = sqlite3.connect('landlord.db')  # Connect to DB
    curs = connection.cursor()  # Cursor tells the database what to do
    curs.execute("DELETE from tenant_list WHERE rowid = (?)", id)
    connection.commit()
    connection.close()