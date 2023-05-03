from tkinter import *
from tkinter import ttk
import database3
import Homepage
import PIL
from PIL import Image, ImageTk

def annualSummary():
  """
  Allows user to access annual summary data
  """

  """Database Initialization"""
  database3.dropTableRentalIncome()
  database3.dropTableExpenseRecord()
  database3.dropTableTenantList()
  database3.createTableTenantList()
  database3.createTableRentalIncome()
  database3.createTableExpenseRecord()
  database3.readRentalIncomeFile()
  database3.readExpenseRecordFile()
  database3.readTenantListFile()

  """Report Creation"""
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
  AnnualReportFile.write(str(rentalSum)+"\n")
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
  for queryList in queryResults:
      index = 0
      for data in queryList:
          if (index < len(queryList) - 1):
              AnnualReportFile.write(str(data) + ", ")
              index += 1
          else:
              AnnualReportFile.write(str(data) + "\n")
  AnnualReportFile.write(str(expenseSum) + "\n")
  """
  Finally, expenses are subtracted from income to show how much money John made (or
  lost) during the year.
  Part C
  """
  total = rentalSum - expenseSum
  AnnualReportFile.write(str(total) + "\n")
  status = ""
  if (total > 0):
      status = "Gained"
  elif (total < 0):
      status = "Lost"
  else:
      status = "Nothing Gained/Lost"
  AnnualReportFile.close()

  """Window Initialization"""
  #Create the main window
  annSumWindow = Tk()
  annSumWindow.geometry('640x360')
  annSumWindow.title('Annual Summary')
  annSumWindow['bg'] = 'white'
  annSumWindow.config(bg='white')
  font = ("Arial", 8)
  title_font = ("Arial bold", 18)

  """Window Commands"""

  def homePage():
      # Return user to the login page.
      annSumWindow.destroy()
      Homepage.homepage()

  """Window Contents"""
  # Read the annual summary from the file
  with open('annualreport.txt', 'r') as file:
    lines = file.readlines()
    rental_sum = float(lines[0].strip())
    categories = [line.strip().split(',') for line in lines[1:6]]
    expense_sum = float(lines[6].strip())
    amount_gained = float(lines[7].strip())
  file.close()
  # Create a widget Frame to display the annual summary
  frame = Frame(annSumWindow, bd=2, relief=SOLID, bg='white')
  frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

  # Add a label for the title of the page
  Label(frame,
        text="Annual Summary",
        font=title_font,
        padx=20,
        pady=20,
        bg='white').pack(expand=True, fill=BOTH)

  # Add a label for rental sum
  Label(frame,
        text=f"Rental sum: ${rental_sum:.2f}",
        font=font,
        padx=20,
        pady=5,
        bg='white').pack(fill=X)
  # Add labels for expense sum and amount gained
  Label(frame,
        text=f"Expense Sum: ${expense_sum:.2f}",
        font=font,
        padx=20,
        pady=5,
        bg='white').pack(fill=X)
  Label(frame,
        text=f"Amount {status}: ${amount_gained:.2f}",
        font=font,
        padx=20,
        pady=5,
        bg='white').pack(fill=X)

  # Create a widget Treeview to display the annual summary in a table
  tree = ttk.Treeview(frame, columns=('category', 'amount'), show='headings')

  # Add column headers
  tree.heading('category', text='Budget Category')
  tree.heading('amount', text='Amount Paid')

  # Add each category and the corresponding amount spent to the table
  for category, amount in categories:
    tree.insert('', 'end', values=(category, f'${float(amount):.2f}'))

  # Display the annual summary in the window with a scrollbar
  scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  tree.pack(side=LEFT, fill=BOTH, padx=20, pady=20, expand=True)
  scrollbar.pack(side=RIGHT, fill=Y)

  # Add a button to go back to the homepage
  Button(annSumWindow, text="Homepage", font=font,
         command=homePage).pack(fill=X,
                                         expand=True,
                                         side=BOTTOM,
                                         padx=20,
                                         pady=20)
  # Display the best part of the program
  bestFriend = ImageTk.PhotoImage(PIL.Image.open("profile3.jpg").resize((80, 80)))
  profile_label = Label(annSumWindow, image=bestFriend, bg='white')
  profile_label.image = bestFriend
  profile_label.pack(padx=20, pady=20)
  # Start the main loop
  annSumWindow.mainloop()
