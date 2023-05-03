import database3

#database3.createTableTenantList()
"""
database3.dropTableRentalIncome()
database3.dropTableExpenseRecord()
database3.createTableRentalIncome()
database3.createTableExpenseRecord()


#"""

"""
database3.delRecordRentalIncome('1')
database3.delRecordRentalIncome('2')
database3.delRecordRentalIncome('3')
database3.delRecordRentalIncome('4')
database3.delRecordExpenseRecord('1')
database3.delRecordExpenseRecord('2')
database3.delRecordExpenseRecord('3')
database3.delRecordExpenseRecord('4')
database3.delRecordTenantList('1')
database3.delRecordTenantList('2')
database3.delRecordTenantList('3')
database3.delRecordTenantList('4')
#database3.addRecordTenantList("John","Smith","101","555-1234","john.smith@example.com")
database3.addRecordRentalIncome(12, 4, 34.54)
database3.addRecordRentalIncome(1, 3, 50.00)
database3.addRecordRentalIncome(5, 1, 47.89)
database3.addRecordRentalIncome(4, 2, 23.45)
database3.addRecordExpenseRecord("APR-30-2023", "Target", "45.66", "MORTGAGE")
database3.addRecordExpenseRecord("JAN-15-2021", "Walmart", "87.98", "REPAIR")
database3.addRecordExpenseRecord("JUL-4-2017", "Starbucks", "23.45", "UTILITIES")
database3.addRecordExpenseRecord("AUG-13-2023", "Steve E. Plus", "193.45", "TAX INSURANCE")

database3.writeRentalIncome()
#database3.displayRentalIncome()
database3.writeExpenseRecord()
database3.writeTenantList()
#database3.displayExpenseRecord()
#database3.delRecordTenantList('1')
database3.delRecordRentalIncome('1')
database3.delRecordRentalIncome('2')
database3.delRecordRentalIncome('3')
database3.delRecordRentalIncome('4')
database3.delRecordExpenseRecord('1')
database3.delRecordExpenseRecord('2')
database3.delRecordExpenseRecord('3')
database3.delRecordExpenseRecord('4')
#database3.readRentalIncomeFile()

#database3.readExpenseRecordFile()

#database3.readTenantListFile()

"""

#database3.displayRentalIncome()
#database3.displayExpenseRecord()
#database3.displayTenantList()

"""
Combines The Rental Income Table with the Tenant Table
From Rental Income: Month, Payment
From Tenants: First Name, Last Name, Apartment Number
"""

#database3.displayPerformQuery("""
#SELECT rental_income.rowid, rental_income.month, rental_income.payment,
#tenant_list.first_name,
#tenant_list.last_name, tenant_list.apartment_number
#FROM rental_income, tenant_list
#WHERE rental_income.tenant_id = tenant_list.rowid
#""")
database3.recordPerformQuery("""
SELECT rental_income.rowid, rental_income.month, rental_income.payment, 
tenant_list.first_name, 
tenant_list.last_name, tenant_list.apartment_number
FROM rental_income, tenant_list
WHERE rental_income.tenant_id = tenant_list.rowid
""", "entirerentalincomerecord.txt")

AnnualReportFile = open("annualreport.txt", "w")
"""
The Annual Report uses data from the Rental Income Record and Expense Record to
summarize how much money came in and how much went out during the year. All the rents are
summed and the result is displayed. 
Part A
"""
rentalSum = float(database3.performQuery("""
SELECT ROUND(SUM(payment),2) FROM rental_income
""")[0][0])
AnnualReportFile.write("Rental Sum: $"+ str(rentalSum)+"\n")
"""
The expenses are summed and displayed by the budget
category, which makes it easy to see, for example, how much was spent on repairs during the
year. 
Part B
"""
queryResults = database3.performQuery("""
SELECT budget_cat, ROUND(SUM(amount_paid), 2) FROM expense_record GROUP BY budget_cat ORDER BY budget_cat
""")
expenseSum = float(database3.performQuery("""
SELECT ROUND(SUM(amount_paid), 2) FROM expense_record
""")[0][0])
AnnualReportFile.write("Budget_Cat  Amount Paid"+ "\n")
AnnualReportFile.write("_______________________"+ "\n")
for queryList in queryResults:
    index = 0
    for data in queryList:
        if (index < len(queryList)-1):
            AnnualReportFile.write(str(data) + ", ")
            index += 1
        else:
            AnnualReportFile.write(str(data)+ "\n")
AnnualReportFile.write("_______________________"+ "\n")
AnnualReportFile.write("Expense Sum: $"+ str(expenseSum)+ "\n")
"""
Finally, expenses are subtracted from income to show how much money John made (or
lost) during the year.
Part C
"""
total = rentalSum-expenseSum
if(total>0):
    AnnualReportFile.write("Gained: $"+ str(total)+ "\n")
elif(total<0):
    AnnualReportFile.write("Lost: $"+ str(total)+ "\n")
else:
    AnnualReportFile.write("Nothing gained or lost."+"\n")
AnnualReportFile.close()
