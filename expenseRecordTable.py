from tkinter import *
from tkinter import ttk
import Homepage
import database3
import PIL
from PIL import Image, ImageTk

def expenseRecordTable():
  """
  Allows user to view the expense record.
  """

  """Database Initialization"""
  database3.dropTableExpenseRecord()
  database3.createTableExpenseRecord()
  database3.readExpenseRecordFile()

  """Window Initialization"""
  # Create the main window
  erTableWindow = Tk()
  erTableWindow.geometry('640x360')
  erTableWindow.title('Expense Record Table')
  erTableWindow['bg'] = 'white'
  erTableWindow.config(bg='white')
  font = ("Arial", 8)
  title_font = ("Arial bold", 18)

  """Window Commands"""
  def homePage():
      #Return user to the login page.
      erTableWindow.destroy()
      Homepage.homepage()

  def orgByDate():
      #Organizes Expense Record by Date, ASC
      database3.recordPerformQuery("""SELECT expense_record.date, expense_record.payee, 
            expense_record.amount_paid, expense_record.budget_cat FROM expense_record 
            ORDER BY expense_record.date""", "tempQuery.txt")
      updateDisplay()

  def orgByPayee():
      #Organizes Expense Record by Payee, ASC
      database3.recordPerformQuery("""SELECT expense_record.date, expense_record.payee, 
            expense_record.amount_paid, expense_record.budget_cat FROM expense_record 
            ORDER BY expense_record.payee""", "tempQuery.txt")
      updateDisplay()

  def orgByAmount():
      #Organizes Expense Record by Amount Paid, ASC
      database3.recordPerformQuery("""SELECT expense_record.date, expense_record.payee, 
            expense_record.amount_paid, expense_record.budget_cat FROM expense_record 
            ORDER BY expense_record.amount_paid""", "tempQuery.txt")
      updateDisplay()

  def orgByCategory():
      #Organizes Expense Record by Budget Category, ASC
      database3.recordPerformQuery("""SELECT expense_record.date, expense_record.payee, 
            expense_record.amount_paid, expense_record.budget_cat FROM expense_record 
            ORDER BY expense_record.budget_cat""", "tempQuery.txt")
      updateDisplay()

  def updateDisplay():
      #Uses the tempquery from one of the org functions and updates the tree to display the new order.
      with open('tempQuery.txt', 'r') as tempFile:
          newExpenses = [line.strip().split(',') for line in tempFile]
      tempFile.close()
      for val in tree.get_children():
          tree.delete(val)
      for newExpense in newExpenses:
          date = newExpense[0]
          payee = newExpense[1]
          amount = "-$" + newExpense[2]  #Add a negative sign to indicate outgoing payment
          category = newExpense[3]
          tree.insert('', 'end', values=(date, payee, amount, category))

  """Window Contents"""
  #Read expense information from the expense_record.txt file
  with open('expense_record.txt', 'r') as file:
    expenses = [line.strip().split(',') for line in file]
  file.close()

  #Create a Frame widget to display the expense list
  frame = Frame(erTableWindow, bd=2, relief=SOLID, bg='white')
  frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

  #Add a label to display the page title
  Label(frame,
        text="Expense Record",
        font=title_font,
        padx=20,
        pady=20,
        bg='white').pack(expand=True, fill=BOTH)

  #Create a Treeview widget to display the expense information as a table
  tree = ttk.Treeview(frame,
                      columns=('date', 'payee', 'amount', 'category'),
                      show='headings')

  #Add column headers
  tree.heading('date', text='Date', command=orgByDate)
  tree.heading('payee', text='Payee',command=orgByPayee)
  tree.heading('amount', text='Amount', command=orgByAmount)
  tree.heading('category', text='Category', command=orgByCategory)

  #Add each expense to the list
  for expense in expenses:
    date = expense[1]
    payee = expense[2]
    amount = "-" + expense[
      3]  # Add a negative sign to indicate outgoing payment
    category = expense[4]
    tree.insert('', 'end', values=(date, payee, amount, category))

  #Display the expense list in the window with a scrollbar
  scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  tree.pack(side=LEFT, fill=BOTH, padx=20, pady=20, expand=True)
  scrollbar.pack(side=RIGHT, fill=Y)

  #Add a button to return to the homepage
  Button(erTableWindow, text="Homepage", font=font,
         command=homePage).pack(fill=X,
                                         expand=True,
                                         side=BOTTOM,
                                         padx=20,
                                         pady=20)

  # Display the best part of the program
  bestFriend = ImageTk.PhotoImage(PIL.Image.open("profile3.jpg").resize((80, 80)))
  profile_label = Label(erTableWindow, image=bestFriend, bg='white')
  profile_label.image = bestFriend
  profile_label.pack(padx=20, pady=20)

  # Launch the main loop
  erTableWindow.mainloop()
