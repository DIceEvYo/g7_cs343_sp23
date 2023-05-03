"""
Group 7 James Lynch, Karla Chuprinski,
Dev Paul, Vu Phan, William Gomez, Camelia Sama
04/30/23
References:
https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/#
https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
https://docs.google.com/document/d/14x8v2uO6NDCCJBbFalxzG08It_grOTvClJ_zzuFdYtY/edit
https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
Image - Google
Sample Data - ChatGpt
"""

import login
import database3 #Used for database initialization

if __name__ == "__main__":
  """
  Database initialization code only needs to run once to create it.
  
  database3.dropTableRentalIncome()
  database3.dropTableExpenseRecord()
  database3.dropTableTenantList()
  database3.createTableTenantList()
  database3.createTableRentalIncome()
  database3.createTableExpenseRecord()
  database3.readRentalIncomeFile()
  database3.readExpenseRecordFile()
  database3.readTenantListFile()
  """

  login.login() #Calling LogIn Page